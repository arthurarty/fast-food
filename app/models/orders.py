from app.models import Database
import psycopg2
import json
from flask import jsonify


class Orders(Database):
    """a restuarant has several orders stored in a list """

    def __init__(self):
        super().__init__()

    def add_order(self, order):
        """add a new order """
        insert_command = "INSERT INTO orders(menu_id, user_id, quantity, created_at) Values (%s, %s, %s, '%s');" % (
            order.menu_id, order.user_id, order.quantity, order.created_at)
        try:
            self.cursor.execute(insert_command)
            self.cursor.execute(
                "SELECT row_to_json(row) FROM (SELECT * FROM orders WHERE user_id = %s AND created_at = '%s') row;" % (order.user_id, order.created_at))
            items = self.cursor.fetchone()
            if items:
                return jsonify({"msg": "Order successfully added"}), 201
            return jsonify({"msg": "Order not added"}), 400
        except psycopg2.IntegrityError:
            return jsonify({"msg": "Menu Item does not exist"}), 404

    def get_orders(self):
        """get all orders from database"""
        return self.query_entire_table('orders')

    def get_single_order(self, id):
        pass

    def update_order_status(self, id, status):
        pass
