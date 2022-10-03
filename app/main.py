# import os
import logging
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from app.config import config

db = SQLAlchemy()
ma = None
secret_key = None
jwt = None
app = None


def create_app(config_name):
    global secret_key, ma, jwt, app
    logging.info('create app')
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config[config_name])
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    config[config_name].init_app(app)
    logging.debug('load config' + str(config[config_name]))
    secret_key = config[config_name].SECRET_KEY
    db.init_app(app)
    ma = Marshmallow(app)
    jwt = JWTManager(app)
    from .resources.version import VersionResource
    app.add_url_rule('/', view_func=VersionResource.as_view('version'))
    # from .resources.auth import UserResource,RegisterResource,RoleResource
    # app.add_url_rule('/register/<string:key>',view_func=RegisterResource.as_view('register'))
    # app.add_url_rule('/login', view_func=UserResource.as_view('login'))
    # app.add_url_rule('/role', view_func=RoleResource.as_view('role'))
    from .resources.comic import ComicResources
    app.add_url_rule('/comic', view_func=ComicResources.as_view('comic_recommend'))
    return app
