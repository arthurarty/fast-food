from flask import Flask, jsonify


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
    if not password:
        return jsonify({"msg": "password field is empty"})

    if not email:
        return jsonify({"msg": "email field is empty"}), 400

def create_jwt_token(db_conn, email, create_access_token):
    user_id = db_conn.return_id(email)
    user_role = db_conn.return_role(email)
    user_details = {"user_id" : " ", "user_role" : " "}
    user_details['user_id'] = user_id[0]
    user_details['user_role'] = user_role[0]
    access_token = create_access_token(identity=user_details)
    output = {'message': 'Successful login'}
    access_token_output = {'access_token': "%s" % (access_token)}
    return jsonify(output, access_token_output), 200