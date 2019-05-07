from flask import Blueprint, jsonify
from flask import request

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
