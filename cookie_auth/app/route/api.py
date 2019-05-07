from flask import Blueprint, jsonify
from flask import request
from flask import session

from app.model import db, User

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/register', methods=['POST'])
def new_user():
    username = request.json['username']
    password = request.json['password']
    print('{} {}'.format(username, password))

    user = User(username=username, password=password)
    db.session.merge(user)
    db.session.commit()

    return jsonify({"status": "success"})


@bp.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    print('{} {}'.format(username, password))

    exists = db.session.query(User).filter_by(username=username, password=password).scalar() is not None

    if exists:
        session['user_id'] = username

        return jsonify({"status": "success"})

    return jsonify({"status": "fail"})
