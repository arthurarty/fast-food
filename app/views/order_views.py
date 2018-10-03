"""File contains order_views"""
from flasgger import swag_from
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app import app
from app.models.order import Order
from app.utilities import (check_for_quantity_and_menuid, test_int_input)
from app.views import db_conn


@app.route('/v1/users/orders', methods=['POST'])
@jwt_required
@swag_from('../docs/post_order.yml')
def post_order():
    """method to add order"""
    current_user = get_jwt_identity()
    menu_id = test_int_input(request.json.get('menu_id'))
    quantity = test_int_input(request.json.get('quantity'))
    output = check_for_quantity_and_menuid(
        request.json.get('quantity'), request.json.get('menu_id'))
    if quantity and menu_id:
        new_order = Order(menu_id, current_user['user_id'], quantity)
        return db_conn.add_order(new_order)

    if output:
        return jsonify({"msg": output}), 400
    return jsonify({"msg": "Menu_id and Quantity must be integers > 0. Example: 2"}), 400


@app.route('/v1/users/orders', methods=['GET'])
@jwt_required
@swag_from('../docs/get_history.yml')
def get_user_history():
    """method returns users history"""
    current_user = get_jwt_identity()
    return jsonify(db_conn.get_orders_by_userid(current_user['user_id'])), 200


@app.route('/v1/orders', methods=['GET'])
@jwt_required
@swag_from('../docs/get_order.yml')
def get_orders():
    """method returns all orders"""
    current_user = get_jwt_identity()
    if not current_user['user_role']:
        return jsonify({'msg': 'Not authorized'}), 403
    res = db_conn.get_orders()
    return jsonify(res), 200


@app.route('/v1/orders/<int:order_id>/', methods=['GET'])
@jwt_required
@swag_from('../docs/get_single_order.yml')
def get_specific_order(order_id):
    """method returns specific order"""
    current_user = get_jwt_identity()
    if not current_user['user_role']:
        return jsonify({'msg': 'Not authorized'}), 403
    res = db_conn.get_single_order(order_id)
    if not res:
        return jsonify({'msg': 'Order not found'}), 404

    return jsonify(res), 200


@app.route('/v1/orders/<int:order_id>/', methods=['PUT'])
@jwt_required
@swag_from('../docs/update_order.yml')
def update_status(order_id):
    """method updates the status of an order"""
    current_user = get_jwt_identity()
    if not current_user['user_role']:
        return jsonify({'msg': 'Not authorized'}), 403
    status = request.json.get('status')
    if status not in ['Processing', 'Cancelled', 'Complete']:
        return jsonify({"msg": "Status input has to be Processing, Cancelled or Complete."}), 400

    if status:
        return db_conn.update_order_status(order_id, status)
    return jsonify({"msg": "Status must be a string. Example: complete"}), 400
