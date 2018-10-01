"""This file contains the database class that contains all database related methods"""
from pprint import pprint
from urllib.parse import urlparse
from flask import jsonify
import psycopg2
import os


class Database:
    def __init__(self, database_url):
        try:
            result = urlparse(database_url)
            username = 'postgres'
            password = 'asP2#fMe'
            database = result.path[1:]
            hostname = result.hostname
            portno = 5432
            self.connection = psycopg2.connect(
                database=database,
                user=username,
                password=password,
                host=hostname,
                port=portno
            )
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pprint("Cannot connect to database")

    def create_table(self, table_name, table_columns):
        """method creates a single table"""
        create_table_command = "CREATE TABLE IF NOT EXISTS %s(%s);" % (
            table_name, table_columns)
        self.cursor.execute(create_table_command)

    def drop_table(self, table_name):
        """method drops a single table from the database"""
        drop_table_command = "DROP TABLE %s" % (table_name)
        self.cursor.execute(drop_table_command)

    def create_all_tables(self):
        """method creates the tables needed for the application"""
        self.create_table('users', "user_id SERIAL PRIMARY KEY, email text " +
                          " NOT NULL UNIQUE, name text NOT NULL, password text NOT NULL, role boolean NOT NULL")
        self.create_table('menu', "menu_id SERIAL PRIMARY KEY, name text " +
                          " NOT NULL UNIQUE, description text NOT NULL, price int NOT NULL")
        self.create_table('orders', "order_id SERIAL PRIMARY KEY, menu_id INT NOT NULL " +
                          "REFERENCES menu(menu_id), user_id INT NOT NULL " +
                          "REFERENCES users(user_id), quantity INT NOT NULL, " +
                          "status text, created_at Date NOT NULL, updated_at Date")

    def drop_all_tables(self):
        self.drop_table('orders')
        self.drop_table('users')
        self.drop_table('menu')

    def check_table(self, table_name):
        """check if a table exists in the database"""
        self.cursor.execute(
            "select exists(select * from information_schema.tables where table_name='%s')" % (table_name))
        return self.cursor.fetchone()[0]

    def check_tables(self):
        """check if all required tables are present"""
        self.check_table('users')
        self.check_table('menu')
        self.check_table('orders')

    def query_single(self, email):
        """returns a user given the user's email"""
        self.cursor.execute("SELECT * FROM users WHERE email = '%s'" % (email))
        item = self.cursor.fetchone()
        return item

    def query_entire_table(self, table_name):
        """returns all records in table"""
        self.cursor.execute("SELECT row_to_json(row) FROM (SELECT * FROM %s) row" %
                            (table_name))
        items = self.cursor.fetchall()
        return items

    def query_single_row(self, table_name, table_column, row_id):
        """returns a single row from table_name where table_column = row_id"""
        self.cursor.execute("SELECT row_to_json(row) FROM (SELECT * FROM %s WHERE %s = '%s') row" %
                            (table_name, table_column, row_id))
        item = self.cursor.fetchone()
        return item

    def return_id(self, email):
        """method returns users's id from databse"""
        self.cursor.execute(
            "SELECT user_id FROM users WHERE email = '%s'" % (email))
        item = self.cursor.fetchone()
        return item

    def return_password(self, email):
        """method returns uers's hashed password from database"""
        self.cursor.execute(
            "SELECT password FROM users WHERE email = '%s'" % (email))
        item = self.cursor.fetchone()
        return item

    def return_role(self, email):
        """method returns uers's hashed password from database"""
        self.cursor.execute(
            "SELECT role FROM users WHERE email = '%s'" % (email))
        item = self.cursor.fetchone()
        return item

    def add_order(self, order):
        """add a new order """
        insert_command = "INSERT INTO orders(menu_id, user_id, quantity, status, created_at) Values (%s, %s, %s, '%s','%s');" % (
            order.menu_id, order.user_id, order.quantity, order.status, order.created_at)
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

    def get_single_order(self, order_id):
        """return a single from the database"""
        return self.query_single_row('orders', 'order_id', order_id)

    def update_order_status(self, order_id, status):
        """update the staus of an order"""
        update_command = "Update orders SET status = '%s' WHERE order_id = '%s'" % (
            status, order_id)
        try:
            self.cursor.execute(
                "SELECT row_to_json(row) FROM (SELECT * FROM orders WHERE order_id = %s) row;" % (order_id))
            items = self.cursor.fetchone()
            if items:
                self.cursor.execute(update_command)
                return jsonify({"msg": "Order updated"}), 201
            else:
                return jsonify({"msg": "Order not found"}), 404
        except:
            return jsonify({"msg": "Error"}), 404

    def get_orders_by_userid(self, user_id):
        """return all orders belonging to a particular user"""
        select_command = "SELECT row_to_json(row) FROM (SELECT * FROM orders WHERE user_id = %s) row;" % (
            user_id)
        self.cursor.execute(select_command)
        return self.cursor.fetchall()
