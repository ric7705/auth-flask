import base64
from functools import wraps

from flask import redirect
from flask import request

from app.model import db, User

from flask_jwt_extended import JWTManager

jwt = JWTManager()


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
