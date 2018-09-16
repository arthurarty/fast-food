from app.views import app
from app.models.order import Order
from flask import Flask, jsonify, request

empty_field = {'msg': 'A field is empty'}

@app.route('/v1/orders', methods=['POST'])
def post_order():
    """method to add order"""
    title = str(request.json.get('customer_name')).strip()

    if not title:
        return jsonify({"msg": "Customer field is empty"}), 400

    if request.json.get('customer_name'):
        new_order = Order('Nangai', 'Chapati', '10')
        return jsonify({"msg": "Order has been added"}), 201

    else:
        output = empty_field
        return jsonify(output), 400