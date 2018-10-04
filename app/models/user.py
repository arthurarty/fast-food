"""File contains user class"""
import psycopg2
from flask import jsonify

from app import app
from app.models import Database


class User(Database):
    """
    Class user represents a user of a system
    it includes methods that add a user to the
    datbase
    """

    def __init__(self, email, name, password, role):
        super().__init__(app.config['DATABASE_URL'])
        self.email = email
        self.name = name
        self.password = password
        self.role = role

    def insert_new_record(self):
        """method inserts new user into db"""
        return self.add_user(self.email, self.name, self.password, self.role)

    def delete_user_from_db(self):
        """deletes users from db"""
        delete_command = "DELETE FROM users WHERE email = %s;", (self.email,)
        self.cursor.execute(delete_command)
