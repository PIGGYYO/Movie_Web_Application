import pytest

from flask import session
from movie_web_app.domain.model import Movie, Actor, Director, Genre, Review, User


def test_register(client):
    response_code = client.get('/authentication/register').status_code
    assert response_code == 200

    response = client.post(
        '/authentication/register',
        data={'user_name': 'kurisu', 'password': '1234Qwer'}
    )
    assert response.headers['Location'] == 'http://localhost/authentication/login'

'''
@pytest.mark.parametrize(('username', 'password', 'message'), (
        ('', '', b'Username is required'),
        ('1', '1', b'Username is too short'),
        ('test', '', b'Password is required'),
        ('test', 'test', b'Password must be at least 6 characters, and contain an upper case letter, \
            a lower case letter and a digit'),
        ('kurisu', 'Test#6^0', b'Your username is already taken - please supply another'),
))
def test_register_with_invalid_input(client, username, password, message):
    response = client.post(
        '/authentication/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data
'''


def test_login(client, auth,in_memory_repo):
    client.post(
        '/authentication/register',
        data={'user_name': 'kurisu', 'password': '1234Qwer'}
    )
    response = auth.login()
    assert response.headers['Location'] == 'http://localhost/'

    with client:
        client.get('/')
        assert session['username'] == 'kurisu'


def test_logout(client, auth):
    client.post(
        '/authentication/register',
        data={'user_name': 'kurisu', 'password': '1234Qwer'}
    )
    auth.login()

    with client:
        auth.logout()
        assert 'username' not in session


def test_login_required_to_comment(client):
    response = client.post('/comment')
    assert response.headers['Location'] == 'http://localhost/authentication/login'


def test_comment(client, auth):
    client.post(
        '/authentication/register',
        data={'user_name': 'kurisu', 'password': '1234Qwer'}
    )
    auth.login()
    response = client.get('/comment?title=Guardians+of+the+Galaxy')
    response = client.post(
        '/comment?title=Guardians+of+the+Galaxy',
        data={'comment': '=w=?ss', 'rating': '10', 'title': 'Guardians of the Galaxy'}
    )
    assert b'=w=?ss' in response.data


@pytest.mark.parametrize(('comment', 'rating','messages'), (
        ('Hey', '10',(b'Your comment is too short')),
        ('ass', '',(b'Rating is required'))))
def test_comment_with_invalid_input(client, auth, comment,rating,messages):
    client.post(
        '/authentication/register',
        data={'user_name': 'kurisu', 'password': '1234Qwer'}
    )
    auth.login()

    response = client.post(
        '/comment?title=Guardians+of+the+Galaxy',
        data={'comment': comment, 'rating': rating, 'title': 'Guardians of the Galaxy'}
    )
    for message in messages:
        assert message in response.data


@pytest.mark.parametrize(('name1', 'name2','name3'), (
        ('Noomi Rapace', 'Logan Marshall-Green','/'),
        ('Noomi Rapace', '/','/')))
def test_movie_with_actor(client,name1,name2,name3):
    response = client.post(
        '/search_by_actor',
        data={'name1': name1, 'name2': name2, 'name3': name3}
    )
    assert b'Noomi Rapace' in response.data


@pytest.mark.parametrize(('name1', 'name2','name3'), (
        ('Action', 'Adventure','/'),
        ('Action', '/','/')))
def test_movie_with_genre(client,name1,name2,name3):
    response = client.post(
        '/search_by_genre',
        data={'name1': name1, 'name2': name2, 'name3': name3}
    )
    assert b'Action' in response.data


def test_movie_with_director(client):
    response = client.post(
        '/search_by_director',
        data={'director_full_name': 'Ridley Scott'}
    )
    assert b'Ridley Scott' in response.data
