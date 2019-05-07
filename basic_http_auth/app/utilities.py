from functools import wraps

from flask import Response
from flask import request
from sqlalchemy import exists

from app.model import db
from app.model import User


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    exist = db.session.query(exists().where(User.username == username and User.password == password)).scalar()
    print(exist)
    return exist


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})


# 需要認證的頁面要掛上這個decorator
# 從request去抓資訊進行check
# 若未認證(client request的header沒帶Authorization欄位, 或身份驗證不對), 回傳401
# 若pass, 則回傳所請求的頁面或資源
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated