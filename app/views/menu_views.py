from app.views import app
from app.utilities import test_str_input, test_int_input
from app.models.menu import Menu
from app.models.food import Food
from flask import Flask, jsonify, request
from flask_jwt_extended import (JWTManager, get_jwt_identity, jwt_required)
menu = Menu()


@app.route('/v1/menu', methods=['POST'])
@jwt_required
def post_menu():
    """method to add order"""
    current_user = get_jwt_identity()
    if not current_user['user_role']:
        return jsonify({'msg':'Not authorized'}), 401

    food_name = test_str_input(request.json.get('food_name'))
    desc = test_str_input(request.json.get('desc'))
    price = test_int_input(request.json.get('price'))

    if not request.json.get('food_name'):
        return jsonify({"msg": "Food_name is missing"}), 400
    if not request.json.get('desc'):
        return jsonify({"msg": "Desc is missing"}), 400
    if not request.json.get('price'):
        return jsonify({"msg": "Price is missing"}), 400

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
def get_menu():
    """method return menu"""
    res = menu.get_menu()
    return jsonify(res), 200
