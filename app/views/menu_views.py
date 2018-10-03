"""File contains menu views"""
from flasgger import swag_from
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app import app
from app.models.food import Food
from app.models.menu import Menu
from app.utilities import check_menu_creation, test_int_input, test_str_input

menu = Menu()


@app.route('/v1/menu', methods=['POST'])
@jwt_required
@swag_from('../docs/post_menu.yml')
def post_menu():
    """method to add order"""
    current_user = get_jwt_identity()
    if not current_user['user_role']:
        return jsonify({'msg': 'Not authorized'}), 403

    output = check_menu_creation(request.json.get(
        'food_name'), request.json.get('desc'), request.json.get('price'))
    if output:
        return jsonify({"msg": output}), 400
    food_name = test_str_input(request.json.get('food_name'))
    desc = test_str_input(request.json.get('desc'))
    price = test_int_input(request.json.get('price'))

    if food_name:
        if desc:
            if price:
                new_menu_item = Food(food_name, desc, price)
                menu.insert_new_food(new_menu_item)
            else:
                return jsonify({"msg": "Price must be an integer > 0. Example: 2"}), 400

        else:
            return jsonify({"msg": "Desc name must be a string. Example: Well done matooke."}), 400
        return jsonify({"msg": "Food has been added"}), 201

    else:
        output = ({"msg": "Name must be a string. Example: Matooke"})
        return jsonify(output), 400


@app.route('/v1/menu', methods=['GET'])
@jwt_required
@swag_from('../docs/get_menu.yml')
def get_menu():
    """method returns menu"""
    res = menu.get_menu()
    return jsonify(res), 200
