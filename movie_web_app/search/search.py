# search.py
from flask import Blueprint, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

import movie_web_app.adapters.repository as repo

# Configure Blueprint.
search_blueprint = Blueprint('search_bp', __name__)


@search_blueprint.route('/search', methods=['GET', 'POST'])
def find_movie():
    form = RegistrationForm()
    if form.validate_on_submit():
        movie = repo.repo_instance.get_movie(form.movie_name.data)
        return render_template('home/home.html')  # list_movie

    return render_template('search/find_movie.html',
                           form=form,
                           handler_url=url_for('search_bp.find_movie'))


class RegistrationForm(FlaskForm):
    movie_name = StringField("Movie Name", [DataRequired(message='Movie_name is required')])
    submit = SubmitField('Find')
