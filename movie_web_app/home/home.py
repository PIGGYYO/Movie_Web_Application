from flask import Blueprint, render_template, url_for

home_blueprint = Blueprint('home_bp', __name__)


@home_blueprint.route('/', methods=['GET'])
def home():
    return render_template(
        'home/home.html',
        find_movie_url= url_for('search_bp.find_movie')
    )