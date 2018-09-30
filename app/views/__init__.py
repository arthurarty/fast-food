from flask import Flask, jsonify, request
from app import create_app
from app.models import Database


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


app = create_app()
db_conn = Database()

#check if tables exist
if not db_conn.check_tables():
    db_conn.create_all_tables()

#import auth views 
from app.views import auth_views

#import menu views
from app.views import menu_views

# import order views
from app.views import order_views
