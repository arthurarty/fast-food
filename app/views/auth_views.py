"""File contains sign up and sign in views"""
from flask import jsonify, request
from werkzeug.security import check_password_hash
from flasgger import swag_from
from app import app
from app.utilities import test_str_input, create_jwt_token, check_for_email_password, signup_user
from app.views import db_conn


@app.route('/v1/auth/signup', methods=['POST'])
@swag_from('../docs/signup.yml')
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
        return jsonify({"msg": "Role field is empty"}), 400

    if email and name and password and role:
        return signup_user(email, name, password, role)

    return jsonify({"msg": "empty field"}), 400


@app.route('/v1/auth/login', methods=['POST'])
@swag_from('../docs/signin.yml')
def login():
    """method logs in user and outputs jwt token"""
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
            return create_jwt_token(db_conn, email)
    return jsonify({"msg": "Bad username or password"}), 400
