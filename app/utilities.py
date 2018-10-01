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


def test_input_form(email, name, password, role):
    if not isinstance(email, str):
        return jsonify({"msg": "Email must be a string. Example: john@exam.com"}), 400

    email.strip()
    if not email:
        return jsonify({"msg": "Email field is empty."}), 400

    if not isinstance(name, str):
        return jsonify({"msg": "Name must be a string. Example: johndoe"}), 400

    name.strip()
    if not name:
        return jsonify({"msg": "Name field is empty"}), 400
    password = str(password).strip()

    if not role:
        return jsonify({"msg": "Role field is empty"}), 400
