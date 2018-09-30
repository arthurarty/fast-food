from flask import Flask, jsonify, request
from app import create_app
from app.models import Database

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
