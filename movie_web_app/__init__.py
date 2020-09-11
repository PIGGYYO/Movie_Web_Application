# __init__.py
from flask import Flask, request
from movie_web_app.adapters.memory_repository import MemoryRepository
import movie_web_app.adapters.repository as repo


def create_app():
    app = Flask(__name__)

    # Create the MemoryRepository implementation for a memory-based repository.
    repo.repo_instance = MemoryRepository()

    # Configure the app from configuration-file settings
    app.config.from_object('config.Config')

    with app.app_context():
        # Register blueprints.
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .search import search
        app.register_blueprint(search.search_blueprint)

    return app

