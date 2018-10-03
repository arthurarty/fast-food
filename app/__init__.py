from flask import Flask, request, jsonify
import json
from flasgger import Swagger
from flask_jwt_extended import JWTManager
from config import DevelopmentConfig

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(DevelopmentConfig)
swag = Swagger(app)
app.config['JWT_SECRET_KEY'] = 'qweBas12@!asBASD'
JWTManager(app)
