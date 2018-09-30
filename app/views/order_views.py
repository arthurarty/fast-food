from app.views import app, test_str_input, test_int_input
from app.models.order import Order
from app.models.orders import Orders
from flask import Flask, jsonify, request
from flask_jwt_extended import (JWTManager, get_jwt_identity, jwt_required)
orders = Orders()


@app.route('/v1/users/orders', methods=['POST'])
@jwt_required
def post_order():
    """method to add order"""
    current_user = get_jwt_identity()
    menu_id = test_int_input(request.json.get('menu_id'))
    quantity = test_int_input(request.json.get('quantity'))

    if not request.json.get('quantity'):
        return jsonify({"msg": "Quantity is missing"}), 400
    
    if not request.json.get('menu_id'):
        return jsonify({"msg":"Menu_id is missing"}), 400

    if quantity and menu_id:
        new_order = Order( menu_id, current_user['user_id'], quantity)
        return orders.add_order(new_order)
    else:
        return jsonify({"msg": "Menu_id and Quantity must be integers > 0. Example: 2"}), 400


@app.route('/v1/orders', methods=['GET'])
@jwt_required
def get_orders():
    """method returns all orders"""
    current_user = get_jwt_identity()
    if not current_user['user_role']:
        return jsonify({'msg':'Not authorized'}), 401
    res = orders.get_orders()
    return jsonify(res), 200


# @app.route('/v1/orders/<int:order_id>/', methods=['GET'])
# @jwt_required
# def get_specific_order(order_id):
#     """method returns specific order"""
#     res = fast_food.get_single_order(order_id)
#     if not res:
#         return jsonify({'msg': 'Order not found'}), 404

#     return jsonify(res), 200


# @app.route('/v1/orders/<int:order_id>/', methods=['PUT'])
# @jwt_required
# def update_status(order_id):
#     """method updates the status of an order"""
#     status = request.json.get('status')
#     if not status == 'complete':
#         return jsonify({"msg": "Status input has to be complete."}), 400

#     if status:
#         res = fast_food.update_order_status(order_id, status)
#         if not res:
#             return jsonify({'msg': 'Order not found'}), 404
#         return jsonify(res), 201
#     else:
#         return jsonify({"msg": "Status must be a string. Example: complete"}), 400
