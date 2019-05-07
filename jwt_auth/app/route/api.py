from flask import Blueprint, jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
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

    exists = db.session.query(User).filter_by(username=username, password=password).scalar() is not None

    if exists:
        access_token = create_access_token(identity=username)
        print('tk:{}'.format(access_token))
        return jsonify(access_token=access_token), 200

    return jsonify({"status": "fail"}), 401


@bp.route('/get_members')
@jwt_required
def get_members():

    users = User.query.all()

    result = []
    for user in users:
        result.append(user.to_json())
    return jsonify({"status": "success", "members": result})
