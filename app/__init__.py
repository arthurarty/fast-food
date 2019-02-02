"""
Create instance of Flask application.
"""
from flask import Flask
from flasgger import Swagger
from flask_jwt_extended import JWTManager
from config import DevelopmentConfig
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(DevelopmentConfig)
swag = Swagger(app)
JWTManager(app)
CORS(app)
