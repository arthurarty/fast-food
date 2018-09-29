from app.views import app, test_str_input, test_int_input
from app.models.menu import Menu
from flask import Flask, jsonify, request
from flask_jwt_extended import (JWTManager, get_jwt_identity, jwt_required)
menu = Menu()

# @app.route('/v1/orders', methods=['POST'])
# @jwt_required
# def post_order():
#     """method to add order"""
#     customer_name = test_str_input(request.json.get('customer_name'))
#     item_name = test_str_input(request.json.get('item_name'))
#     quantity = test_int_input(request.json.get('quantity'))

#     if not request.json.get('customer_name'):
#         return jsonify({"msg": "Customer_name missing"}), 400
#     if not request.json.get('item_name'):
#         return jsonify({"msg": "Item_name missing"}), 400
#     if not request.json.get('quantity'):
#         return jsonify({"msg": "Quantity is missing"}), 400

#     if customer_name:
#         if item_name:
#             if quantity:
#                 new_order = Order(customer_name, item_name, quantity)
#                 fast_food.add_order(new_order)
#             else:
#                 return jsonify({"msg": "Quantity must be an integer > 0. Example: 2"}), 400

#         else:
#             return jsonify({"msg": "Item name must be a string. Example: Rice"}), 400
#         return jsonify({"msg": "Order has been added"}), 201

#     else:
#         output = ({"msg": "Name must be a string. Example: johndoe"})
#         return jsonify(output), 400


@app.route('/v1/menu', methods=['GET'])
@jwt_required
def get_menu():
    """method return menu"""
    res = menu.get_menu()
    return jsonify(res), 200