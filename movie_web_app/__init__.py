# __init__.py
from flask import Flask, request, session
import os
from movie_web_app.adapters.memory_repository import MemoryRepository, read_csv_file
import movie_web_app.adapters.repository as repo


def create_app():
    app = Flask(__name__)

    # Create the MemoryRepository implementation for a memory-based repository.
    repo.repo_instance = MemoryRepository()
    data_path = os.path.join('movie_web_app', 'adapters', 'datafiles')

    # Configure the app from configuration-file settings
    app.config.from_object('config.Config')

    with app.app_context():
        # Register blueprints.
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .search import search
        app.register_blueprint(search.search_blueprint)

        from .movies import movies
        app.register_blueprint(movies.movies_blueprint)

        from .authentication import authentication
        app.register_blueprint(authentication.authentication_blueprint)

    repo.repo_instance = MemoryRepository()
    read_csv_file(os.path.join(data_path, 'Data1000Movies.csv'),repo.repo_instance)

    return app
