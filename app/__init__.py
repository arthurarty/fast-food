from flask import Flask, request, jsonify
import json


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    return app
