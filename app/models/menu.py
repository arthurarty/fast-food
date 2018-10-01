"""the menu class"""
from app.models import Database
import psycopg2
import json
from flask import jsonify


class Menu(Database):
    def __init__(self, database_url):
        super().__init__(database_url)

    def insert_new_food(self, food):
        """method creates a single table"""
        insert_command = "INSERT INTO menu(name, description, price) Values('%s', '%s', '%s'); " % (food.name, food.description, food.price)
        self.cursor.execute(insert_command)

    def get_menu(self):
        """method returns all food in menu"""
        return self.query_entire_table('menu')
