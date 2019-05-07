import base64
from functools import wraps

from flask import redirect, jsonify
from flask import request
from flask import session

from app.model import db, User


def token_check(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        '''for API
        '''
        token_type, credential = request.headers.get('Authorization').split(' ')

        exists = db.session.query(User).filter_by(token=credential).scalar() is not None

        if not exists:
            return jsonify({"status": "fail", "members": []})
        return fn(*args, **kwargs)
    return wrapper


def login_required(fn):
    '''for page
    '''
    @wraps(fn)
    def wrapper(*args, **kwargs):
        req_token = request.args.get('token')

        try:
            token_type, credential = base64.standard_b64decode(req_token).decode("utf-8").split(' ')
            exists = db.session.query(User).filter_by(token=credential).scalar() is not None
            if not exists:
                return redirect('/login')
            return fn(*args, **kwargs)

        except:
            return redirect('/login')

    return wrapper
