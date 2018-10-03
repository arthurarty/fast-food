from flask import Flask, jsonify, request, redirect
from app import app
from app.models import Database

db_conn = Database(app.config['DATABASE_URL'])


# check if tables exist
if not db_conn.check_tables():
    db_conn.create_all_tables()

# import auth views
from app.views import auth_views

# import menu views
from app.views import menu_views

# import order views
from app.views import order_views


@app.route("/")
def main():
    """redirect / to apidocs"""
    return redirect("apidocs/")


@app.errorhandler(400)
def bad_request(error):
    """custom error message for 400"""
    return jsonify({"msg": "Bad reqeust"}), 400


@app.errorhandler(401)
def not_authorized(error):
    """custom error message for 400"""
    return jsonify({"msg": "Not authorized."}), 401


@app.errorhandler(403)
def forbidden(error):
    """custom error message for 400"""
    return jsonify({"msg": "Forbidden."}), 403


@app.errorhandler(404)
def page_not_found(error):
    """custom error message for 400"""
    return jsonify({"msg": "Route does not exist"}), 404


@app.errorhandler(405)
def method_not_allowed(error):
    """custom error message for 400"""
    return jsonify({"msg": "Method not allowed"}), 405
