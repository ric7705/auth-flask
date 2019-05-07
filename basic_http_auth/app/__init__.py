from flask import Flask

from .utilities import requires_auth
from app.model import db
from app.route import pages, api


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # init db
    db.init_app(app)
    db.app = app
    db.create_all()

    app.register_blueprint(pages.bp)
    app.register_blueprint(api.bp)

    return app
