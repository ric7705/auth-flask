from functools import wraps

from flask import redirect
from flask import session
from flask import url_for


def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not session.get('user_id'):
            return redirect('/login')
        return fn(*args, **kwargs)
    return wrapper