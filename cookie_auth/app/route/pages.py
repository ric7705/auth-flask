from flask import Blueprint
from flask import render_template

from app.model import User
from app.utilities import login_required

bp = Blueprint('pages', __name__)


@bp.route('/')
def home():
    return render_template('home.html', title='cookie auth')


@bp.route('/register')
def register():
    return render_template('register.html')


@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/protected_page')
@login_required
def secret_page():
    users = User.query.all()
    print(type(users))
    return render_template('protected_page.html', users=users)
