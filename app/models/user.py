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
        insert_command = "INSERT INTO users(email, name, password, role) VALUES('%s', '%s', '%s', '%s');" % (
            self.email, self.name, self.password, self.role,)
        try:
            self.cursor.execute(insert_command)
            self.cursor.execute(
                "SELECT * FROM users WHERE email = '%s';" % (self.email,))
            item = self.cursor.fetchone()
            if item:
                return jsonify({"msg": "User successfully created"}), 201
        except psycopg2.IntegrityError:
            output = {
                'message': 'Email address already exists: ',
            }
            return jsonify(output), 400

    def delete_user_from_db(self):
        """deletes users from db"""
        delete_command = "DELETE FROM users WHERE email = %s;", (self.email,)
        self.cursor.execute(delete_command)
