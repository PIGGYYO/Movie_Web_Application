# movies.py
from flask import Blueprint, render_template, url_for, redirect, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

import movie_web_app.adapters.repository as repo

# Configure Blueprint.
movies_blueprint = Blueprint('movies_bp', __name__)


@movies_blueprint.route('/display', methods=['GET'])
def display_movies():
    per_page = 5
    cursor = request.args.get('cursor')

    if cursor is None:
        cursor = 0
    else:
        cursor = int(cursor)

    movie_ids = []
    for i in range(cursor, cursor + per_page):
        movie_ids += [i]
    movies = []
    for id in movie_ids:
        movies += [repo.repo_instance.dataset_of_movies[id]]

    first_movie_url = None
    last_movie_url = None
    prev_movie_url = None

    next_movie_url = url_for('movies_bp.display_movies', cursor = cursor + per_page)

    if cursor > 0:
        prev_movie_url = url_for('movies_bp.display_movies', cursor = cursor - per_page)
        first_movie_url = url_for('movies_bp.display_movies')

    if cursor + per_page < len(movie_ids):
        next_movie_url = url_for('movies_bp.display_movies', cursor = cursor + per_page)

        last_cursor = per_page * int(len(movie_ids) / per_page)
        if len(movie_ids) % per_page == 0:
            last_cursor -= per_page
        last_movie_url = url_for('movies_bp.display_movies', cursor=last_cursor)
    print(first_movie_url, last_movie_url,prev_movie_url,next_movie_url)
    print(cursor)
    print(cursor + per_page < len(movie_ids))

    return render_template('movies/display_movies.html',
                           title='Movies',
                           movies=movies,
                           first_movie_url=first_movie_url,
                           last_movie_url=last_movie_url,
                           prev_movie_url=prev_movie_url,
                           next_movie_url=next_movie_url,
                           find_movie_url= url_for('search_bp.find_movie'))
