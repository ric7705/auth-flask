from flask import Blueprint
from flask import render_template

from app.model import User

from app.utilities import login_required

bp = Blueprint('pages', __name__)


@bp.route('/')
def home():
    return render_template('home.html', title='jwt token auth')


@bp.route('/register')
def register():
    return render_template('register.html')


@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/protected_page')
def secret_page():
    return render_template('protected_page.html')
