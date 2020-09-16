# search_movie.py
from flask import Blueprint, render_template, url_for, redirect, request, session
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, TextAreaField, HiddenField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError
from movie_web_app.movies.movies import display_movies
import movie_web_app.adapters.repository as repo
from movie_web_app.authentication.authentication import login_required
from movie_web_app.domain.model import Review

# Configure Blueprint.
search_blueprint = Blueprint('search_bp', __name__)

'''
@search_blueprint.route('/search_movie', methods=['GET', 'POST'])
def find_movie():
    form = FindForm()
    if form.validate_on_submit():
        movie_name = form.movie_name.data
        movie = repo.repo_instance.get_movie(movie_name)
        return render_template('search_movie/print_movie.html',
                               movie = movie)

    return render_template('search_movie/find_movie.html',
                           form=form,
                           handler_url=url_for('search_bp.find_movie'))


class FindForm(FlaskForm):
    movie_name = StringField("Movie Name", [DataRequired(message='Movie name is required')])
    submit = SubmitField('Find')

'''
@search_blueprint.route('/search_by_director', methods=['GET', 'POST'])
def search_by_director():
    form = DirectorForm()
    if form.validate_on_submit():
        director_full_name = form.director_full_name.data
        director = repo.repo_instance.get_director(director_full_name)
        if director is None:
            return render_template('search_movie/lost.html',
                                   title = 'director',
                                   redirect_url = url_for('search_bp.search_by_director'))
        movies = []
        for movie in repo.repo_instance.dataset_of_movies:
            if movie.director == director:
                movies.append(movie)
        return render_template('movies/display_movies.html',
                               movies = movies,
                               title = "Director" + director.__repr__())
    return render_template('search_movie/director.html',
                           form = form,
                           handler_url = url_for('search_bp.search_by_director'))


class DirectorForm(FlaskForm):
    director_full_name = StringField("Director Name",[DataRequired(message='Director name is required')])
    submit = SubmitField('Search by Director')


@search_blueprint.route('/search_by_genre', methods=['GET', 'POST'])
def search_by_genre():
    form = GenreForm()
    if form.validate_on_submit():
        genre1 = form.name1.data
        genre2 = form.name2.data
        genre3 = form.name3.data
        genre1 = repo.repo_instance.get_genre(genre1)
        genre2 = repo.repo_instance.get_genre(genre2)
        genre3 = repo.repo_instance.get_genre(genre3)
        return display_movies('Genre',genre1,genre2,genre3)
    return render_template('search_movie/genre_actor.html',
                           form = form,
                           handler_url = url_for('search_bp.search_by_genre'))


class GenreForm(FlaskForm):
    name1 = StringField("Genre 1",[DataRequired(message='Genre is required')])
    name2 = StringField("Genre 2",[DataRequired(message='Genre is required')])
    name3 = StringField("Genre 3",[DataRequired(message='Genre is required')])
    submit = SubmitField('Search by Genre')


@search_blueprint.route('/search_by_actor', methods=['GET', 'POST'])
def search_by_actor():
    form = ActorForm()
    if form.validate_on_submit():
        actor1 = form.name1.data
        actor2 = form.name2.data
        actor3 = form.name3.data
        actor1 = repo.repo_instance.get_actor(actor1)
        actor2 = repo.repo_instance.get_actor(actor2)
        actor3 = repo.repo_instance.get_actor(actor3)
        return display_movies('Actor',actor1,actor2,actor3)
    return render_template('search_movie/genre_actor.html',
                           form = form,
                           handler_url = url_for('search_bp.search_by_actor'))


class ActorForm(FlaskForm):
    name1 = StringField("Actor 1",[DataRequired(message='Actor is required')])
    name2 = StringField("Actor 2",[DataRequired(message='Actor is required')])
    name3 = StringField("Actor 3",[DataRequired(message='Actor is required')])
    submit = SubmitField('Search by Actor')


@search_blueprint.route('/comment', methods=['GET', 'POST'])
@login_required
def comment_on_movie():
    username = session['username']
    form = CommentForm()
    if form.validate_on_submit():
        title = form.title.data
        review = Review(username, title, form.comment.data, form.rating.data)
        movie = repo.repo_instance.get_movie(title)
        movie.review.append(review)
        movie.add_comment_url = url_for('search_bp.comment_on_movie', title=movie.title)
        return render_template('movies/display_movies.html',
                               title='Review',
                               movies = [movie],
                               first_movie_url=None,
                               last_movie_url=None,
                               prev_movie_url=None,
                               next_movie_url=None)

    if request.method == 'GET':
        title = request.args.get('title')
        form.title.data = title
    else:
        title = form.title.data
    movie = repo.repo_instance.get_movie(title)
    return render_template(
        'search_movie/comment_on_movie.html',
        title='Review',
        movie=movie,
        comment = movie.review,
        form=form,
        handler_url=url_for('search_bp.comment_on_movie'))


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', [
        DataRequired(),
        Length(min=4, message='Your comment is too short')])
    rating = IntegerField('Rating',[
        DataRequired(message='Rating is required')])
    title = HiddenField("Title")
    submit = SubmitField('Submit')
