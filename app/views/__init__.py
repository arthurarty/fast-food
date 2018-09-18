from flask import Flask, jsonify, request
from app import create_app


app = create_app()

# import order views
from app.views import order