from app.models.user import User
import re

from flask import Flask, jsonify, request
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)
from werkzeug.security import check_password_hash, generate_password_hash

from app import app
from app.utilities import *
from app.views import db_conn


@app.route('/v1/auth/signup', methods=['POST'])
def add_user():
    """add user adds a user having validated the inputs."""
    email = test_str_input(request.json.get('email'))
    if not email:
        return jsonify({"msg": "Email field is empty."}), 400

    name = test_str_input(request.json.get('name'))

    if not name:
        return jsonify({"msg": "Name field is empty"}), 400
    password = str(request.json.get('password')).strip()

    role = request.json.get('role')
    if not role:
        return jsonify({"msg":"Role field is empty"}), 400
    
    if email and name and password and role:
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

    return jsonify({"msg": "empty field"}), 400


@app.route('/v1/auth/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    
    email = test_str_input(request.json.get('email'))
    password = test_str_input(str(request.json.get('password')))
    check_for_email_password(email, password)

    output = ""
    items = db_conn.query_single(email)
    output = output + str(items)
    hashed_password = db_conn.return_password(email)

    if email in output:
        if check_password_hash(hashed_password[0], password):
            return create_jwt_token(db_conn, email, create_access_token)
    return jsonify({"msg":"Bad username or password"}), 400
