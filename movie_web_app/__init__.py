# __init__.py
from flask import Flask, request


def create_app():
    app = Flask(__name__)

    # Configure the app from configuration-file settings
    app.config.from_object('config.Config')

    return app

