from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    token = db.Column(db.String(20))
    token_create_dt = db.Column(DateTime)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'token': self.token,
            'token_create_dt': self.token_create_dt,
        }
