from flask import Blueprint
from flask import render_template

from app import db
from app import requires_auth
from app.model import User

bp = Blueprint('pages', __name__)


@bp.route('/')
def home():
    return render_template('home.html', title='basic http auth')


@bp.route('/register')
def register():
    return render_template('register.html')


@bp.route('/protected_page')
@requires_auth
def secret_page():
    users = User.query.all()
    print(type(users))
    return render_template('protected_page.html', users=users)
