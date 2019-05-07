import datetime
from flask import Blueprint, jsonify
from flask import request
from uuid import uuid4

from app.model import db, User

from app.utilities import token_check

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

    exists = db.session.query(User).filter_by(username=username, password=password).scalar() is not None

    if exists:

        token = str(uuid4())
        db.session.query(User).filter_by(username=username, password=password).update({'token': token, 'token_create_dt': datetime.datetime.now()})
        db.session.commit()

        return jsonify({"status": "success", "token": token})

    return jsonify({"status": "fail"})


@bp.route('/get_members')
@token_check
def get_members():

    users = User.query.all()

    result = []
    for user in users:
        result.append(user.to_json())
    return jsonify({"status": "success", "members": result})
