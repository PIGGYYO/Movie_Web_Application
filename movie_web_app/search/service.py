from flask import Blueprint, render_template, url_for, redirect, request, session

import movie_web_app.adapters.repository as repo


def display_movies(movie_list,title,name1,name2,name3):
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
        prev_movie_url = url_for('movies_bp.display_movies', cursor = cursor - per_page)
        first_movie_url = url_for('movies_bp.display_movies')

    if cursor + per_page < len(movie_list):
        next_movie_url = url_for('movies_bp.display_movies', cursor = cursor + per_page)

        last_cursor = per_page * int(len(movie_list) / per_page)
        if len(movie_list) % per_page == 0:
            last_cursor -= per_page
        last_movie_url = url_for('movies_bp.display_movies', cursor=last_cursor)

    return render_template('movies/display_movies.html',
                           title= title,
                           movies=movies,
                           first_movie_url=first_movie_url,
                           last_movie_url=last_movie_url,
                           prev_movie_url=prev_movie_url,
                           next_movie_url=next_movie_url)