from flask import jsonify, redirect, request
from app.views import app
from app.models import Database

if __name__ == '__main__':
    app.run(debug=True)
