# search_movie.py
from flask import Blueprint, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

import movie_web_app.adapters.repository as repo

# Configure Blueprint.
search_blueprint = Blueprint('search_bp', __name__)


@search_blueprint.route('/search_movie', methods=['GET', 'POST'])
def find_movie():
    form = RegistrationForm()
    if form.validate_on_submit():
        movie_name = form.movie_name.data
        movie = repo.repo_instance.get_movie(movie_name)
        return render_template('search_movie/print_movie.html',
                               movie = movie,
                               find_movie_url = url_for('search_bp.find_movie'))

    return render_template('search_movie/find_movie.html',
                           form=form,
                           handler_url=url_for('search_bp.find_movie'),
                           find_movie_url = url_for('search_bp.find_movie'))


class RegistrationForm(FlaskForm):
    movie_name = StringField("Movie Name", [DataRequired(message='Movie_name is required')])
    submit = SubmitField('Find')
