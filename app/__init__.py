from flask import Flask, request, jsonify
import json

from flask_jwt_extended import JWTManager

app = Flask(__name__, instance_relative_config=True)
app.config['JWT_SECRET_KEY'] = 'qweBas12@!asBASD'
JWTManager(app)
