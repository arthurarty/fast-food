from app.views import app, test_str_input, test_int_input
from app.models.order import Order
from app.models.restuarant import Restuarant
from flask import Flask, jsonify, request

fast_food = Restuarant()


@app.route('/v1/orders', methods=['POST'])
def post_order():
    """method to add order"""
    customer_name = test_str_input(request.json.get('customer_name'))
    item_name = test_str_input(request.json.get('item_name'))
    quantity = test_int_input(request.json.get('quantity'))

    if not request.json.get('customer_name'):
        return jsonify({"msg": "Customer_name missing"}), 400
    if not request.json.get('item_name'):
        return jsonify({"msg": "Item_name missing"}), 400
    if not request.json.get('quantity'):
        return jsonify({"msg": "Quantity is missing"}), 400

    if customer_name:
        if item_name:
            if quantity:
                new_order = Order(customer_name, item_name, quantity)
                fast_food.add_order(new_order)
            else:
                return jsonify({"msg": "Quantity must be an integer > 0. Example: 2"}), 400

        else:
            return jsonify({"msg": "Item name must be a string. Example: Rice"}), 400
        return jsonify({"msg": "Order has been added"}), 201

    else:
        output = ({"msg": "Name must be a string. Example: johndoe"})
        return jsonify(output), 400


@app.route('/v1/orders', methods=['GET'])
def get_orders():
    """method returns all orders"""
    res = fast_food.get_orders()
    return jsonify(res), 200


@app.route('/v1/orders/<int:order_id>/', methods=['GET'])
def get_specific_order(order_id):
    """method returns specific order"""
    res = fast_food.get_single_order(order_id)
    if not res:
        return jsonify({'msg': 'Order not found'}), 404

    return jsonify(res), 200


@app.route('/v1/orders/<int:order_id>/', methods=['PUT'])
def update_status(order_id):
    """method updates the status of an order"""
    status = test_str_input(request.json.get('status'))
    if not status == 'complete':
        return jsonify({"msg": "Status input has to be complete."}), 400

    if status:
        res = fast_food.update_order_status(order_id, status)
        if not res:
            return jsonify({'msg': 'Order not found'}), 404
        return jsonify(res), 201
    else:
        return jsonify({"msg": "Status must be a string. Example: complete"}), 400
