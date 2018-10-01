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
