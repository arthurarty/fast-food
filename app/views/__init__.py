from flask import Flask, jsonify, request, redirect
from app import app
from app.models import Database
from config import DevelopmentConfig

app.config.from_object(DevelopmentConfig)
db_conn = Database(app.config['DATABASE_URL'])

@app.route("/")
def main():
    return redirect("apidocs/")

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
