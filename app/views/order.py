from app.views import app
from app.models.order import Order
from app.models.restuarant import Restuarant
from flask import Flask, jsonify, request

empty_field = {'msg': 'A field is empty'}
fast_food = Restuarant()


@app.route('/v1/orders', methods=['POST'])
def post_order():
    """method to add order"""
    title = str(request.json.get('customer_name')).strip()

    if not title:
        return jsonify({"msg": "Customer field is empty"}), 400

    if request.json.get('customer_name'):
        new_order = Order('Nangai', 'Chapati', '10')
        fast_food.add_order(new_order)
        return jsonify({"msg": "Order has been added"}), 201

    else:
        output = empty_field
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
    return jsonify(res), 200
