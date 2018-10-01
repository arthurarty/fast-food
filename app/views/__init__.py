from flask import Flask, jsonify, request
from app import create_app
from app.models import Database

app = create_app()
db_conn = Database()

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"msg": "Bad reqeust"}), 400


@app.errorhandler(401)
def not_authorized(error):
    return jsonify({"msg": "Not authorized."}), 401


@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"msg": "Route does not exist"}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"msg": "Method not allowed"}), 405

#check if tables exist
if not db_conn.check_tables():
    db_conn.create_all_tables()

#import auth views 
from app.views import auth_views

#import menu views
from app.views import menu_views

# import order views
from app.views import order_views
