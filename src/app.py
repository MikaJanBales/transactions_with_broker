import os
from functools import partial

from flask import Flask
from flasgger import Swagger
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy_session import flask_scoped_session


from transactions_with_broker.src.api.inner.urls import inner_api
from transactions_with_broker.db.app import BaseModel, get_connect_string


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = get_connect_string(os.environ)
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    apis = [
        inner_api
    ]
    for blueprint in apis:
        app.register_blueprint(blueprint)

    Swagger(app, parse=True)

    # init db
    db = SQLAlchemy(app)
    session = flask_scoped_session(
        partial(db.create_scoped_session, options={"autoflush": False}),
        app
    )
    BaseModel.query = session.query_property()
    return app


if __name__ == "__main__":
    app = create_app()
