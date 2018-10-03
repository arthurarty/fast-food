"""
Utilites used through out the application
"""
import re

from flask import jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash

from app.models.user import User


def test_str_input(text):
    """test input to be string and not empty"""
    if isinstance(text, str):
        new_text = str(text).strip()
        if not new_text:
            return False
        return new_text
    return False


def test_int_input(number):
    """test input to be int > 0"""
    if isinstance(number, int):
        if number > 0:
            return number
    return False


def check_for_quantity_and_menuid(quantity, menu_id):
    """check if quantity and menuid have been posted"""
    output = ""
    if not quantity:
        output = "Quantity is missing"
    if not menu_id:
        output = "Menu_id is missing"
    return output


def check_for_email_password(email, password):
    """method ensures email and password exist"""
    if not password:
        return jsonify({"msg": "password field is empty"}), 400

    if not email:
        return jsonify({"msg": "email field is empty"}), 400


def create_jwt_token(db_conn, email):
    """method creates jwt token for a user that logs in successfull"""
    user_id = db_conn.return_id(email)
    user_role = db_conn.return_role(email)
    user_details = {"user_id": " ", "user_role": " "}
    user_details['user_id'] = user_id[0]
    user_details['user_role'] = user_role[0]
    access_token = create_access_token(identity=user_details)
    output = {'message': 'Successful login'}
    access_token_output = {'access_token': "%s" % (access_token)}
    return jsonify(output, access_token_output), 200


def signup_user(email, name, password, role):
    """sign up a user given the email, name, password and role"""
    output = ""
    if not re.match(r'^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]+$', email):
        output = "Invalid email. Example: john@exam.com"

    if not re.match(r'^[a-z0-9_]+$', name) or len(name) > 15:
        output = "Name can only contain lowercase a-z, 0-9, _ and Max len of 15"

    if len(password) < 8 or len(password) > 12:
        output = "Password should be 8 chars at least and 12 at most"

    if len(output) > 2:
        return jsonify({"msg": output}), 400

    new_user = User(email, name, generate_password_hash(password), role)
    return new_user.insert_new_record()
