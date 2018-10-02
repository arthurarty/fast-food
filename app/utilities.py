from flask import Flask, jsonify
from flask_jwt_extended import (create_access_token,
                                get_jwt_identity, jwt_required)
from werkzeug.security import check_password_hash, generate_password_hash
from app.models.user import User
import re

def test_str_input(text):
    """test input to be string"""
    if isinstance(text, str):
        """check if string is empty using strip function"""
        new_text = str(text).strip()
        if not new_text:
            """if string empty return false"""
            return False
        return new_text
    else:
        return False


def test_int_input(number):
    """test input to be int"""
    if isinstance(number, int):
        """check if int is greater than 0"""
        if number > 0:
            return number
        else:
            return False
    else:
        return False

def check_for_email_password(email, password):
    """method ensures email and password exist"""
    if not password:
        return jsonify({"msg": "password field is empty"})

    if not email:
        return jsonify({"msg": "email field is empty"}), 400

def create_jwt_token(db_conn, email):
    """method creates jwt token for a user that logs in successfull"""
    user_id = db_conn.return_id(email)
    user_role = db_conn.return_role(email)
    user_details = {"user_id" : " ", "user_role" : " "}
    user_details['user_id'] = user_id[0]
    user_details['user_role'] = user_role[0]
    access_token = create_access_token(identity=user_details)
    output = {'message': 'Successful login'}
    access_token_output = {'access_token': "%s" % (access_token)}
    return jsonify(output, access_token_output), 200

def signup_user(email, name, password, role):
    if not re.match(r'^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return jsonify({"msg": "Invalid email. Example: john@exam.com"}), 400

    if len(name) > 15:
        return jsonify({"msg": "Name is too long, max 15"}), 400

    if not re.match(r'^[a-z0-9_]+$', name):
        return jsonify({"msg": "Name can only contain lowercase a-z, 0-9 and _"}), 400

    if len(password) < 8:
        return jsonify({"msg": "Password too short, min 8 chars"}), 400

    if len(password) > 12:
        return jsonify({"msg": "Password too long, max 12"}), 400

    new_user = User(email, name, generate_password_hash(password), role)
    return new_user.insert_new_record()