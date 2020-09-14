# movies.py
from flask import Blueprint, render_template, url_for, redirect, request, session
from movie_web_app.domain.model import Genre, Actor

import movie_web_app.adapters.repository as repo

# Configure Blueprint.
movies_blueprint = Blueprint('movies_bp', __name__)


@movies_blueprint.route('/display', methods=['GET'])
def display_movies(title = None,name1 = None, name2 = None, name3 = None):
    movie_list = []

    if title is None:
        title = request.args.get('title')
        if title is None:
            title = 'Movies'

    if title == 'Movies':
        movie_list = repo.repo_instance.dataset_of_movies

    if title == 'Genre':
        try:
            if name1 is None:
                name1 = Genre(request.args.get('name1').strip().strip('<').strip('>'))
        except:
            pass
        try:
            if name2 is None:
                name2 = Genre(request.args.get('name2').strip().strip('<').strip('>'))
        except:
            pass
        try:
            if name3 is None:
                name3 = Genre(request.args.get('name3').strip().strip('<').strip('>'))
        except:
            pass

        for movie in repo.repo_instance.dataset_of_movies:
            if name1 is None and name2 is None and name3 is None:
                return render_template('search_movie/lost.html',
                                       title = 'genres',
                                       redirect_url = url_for('search_bp.search_by_genre'))
            if name1 in movie.genres and name2 in movie.genres and name3 in movie.genres:
                movie_list.append(movie)

    if title == 'Actor':
        try:
            if name1 is None:
                name1 = Actor(request.args.get('name1').strip().strip('<').strip('>'))
        except:
            pass
        try:
            if name2 is None:
                name2 = Actor(request.args.get('name2').strip().strip('<').strip('>'))
        except:
            pass
        try:
            if name3 is None:
                name3 = Actor(request.args.get('name3').strip().strip('<').strip('>'))
        except:
            pass

        for movie in repo.repo_instance.dataset_of_movies:
            if name1 is None and name2 is None and name3 is None:
                return render_template('search_movie/lost.html',
                                   title='actors',
                                   redirect_url=url_for('search_bp.search_by_actor'))
            if name1 in movie.actors and name2 in movie.actors and name3 in movie.actors:
                movie_list.append(movie)

    per_page = 6
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
        try:
            movies += [movie_list[id]]
        except:
            pass
    first_movie_url = None
    last_movie_url = None
    prev_movie_url = None
    next_movie_url = None
    if cursor > 0:
        prev_movie_url = url_for('movies_bp.display_movies', cursor = cursor - per_page, title = title, name1 = name1,name2 = name2,name3 = name3)
        first_movie_url = url_for('movies_bp.display_movies', movie_list = movie_list, title = title,name1 = name1,name2 = name2,name3 = name3)

    if cursor + per_page < len(movie_list):
        next_movie_url = url_for('movies_bp.display_movies', cursor = cursor + per_page,title = title,name1 = name1,name2 = name2,name3 = name3)

        last_cursor = per_page * int(len(movie_list) / per_page)
        if len(movie_list) % per_page == 0:
            last_cursor -= per_page
        last_movie_url = url_for('movies_bp.display_movies', cursor=last_cursor,title = title,name1 = name1,name2 = name2,name3 = name3)
    return render_template('movies/display_movies.html',
                           title= title,
                           movies=movies,
                           space1 = name1,
                           space2 = name2,
                           space3 = name3,
                           first_movie_url=first_movie_url,
                           last_movie_url=last_movie_url,
                           prev_movie_url=prev_movie_url,
                           next_movie_url=next_movie_url)
