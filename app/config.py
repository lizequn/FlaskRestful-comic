import os
import sys
import logging
import json

# import urllib.parse


BASEDIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
SECURITY_FILE = os.path.join(BASEDIR, 'security.json')
POETRY_CONFIG_FILE = os.path.join(BASEDIR, 'pyproject.toml')
FILE_FOLDER = os.path.join(BASEDIR, 'files')


def create_sqlite_uri(db_name):
    return "sqlite:///" + os.path.join(BASEDIR, db_name)


# def create_mongodb_uri(db_name, _username, _password):
#     username = urllib.parse.quote_plus(_username)
#     password = urllib.parse.quote_plus(_password)
#     return "mongodb://%s:%s@157.245.47.211:27017/%s" % (username,password,db_name)


class Config(object):
    if not os.path.exists(FILE_FOLDER):
        os.makedirs(FILE_FOLDER)
    with open(SECURITY_FILE) as security:
        security_config = json.load(security)
    SECRET_KEY = security_config.get("SECRET_KEY")
    JWT_SECRET_KEY = security_config.get("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POETRY_CONFIG = POETRY_CONFIG_FILE
    FILE_FOLDER = FILE_FOLDER
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024
    # MONGO_URI_PROD = create_mongodb_uri("path",
    #                                security_config.get("mongodb_username"),
    #                                security_config.get("mongodb_password"))
    # MONGO_URI_DEV = create_mongodb_uri("test",
    #                                     security_config.get("mongodb_test_username"),
    #                                     security_config.get("mongodb_test_password"))
    SQLALCHEMY_DATABASE_URI = create_sqlite_uri('app.db')
    logging.basicConfig(stream=sys.stdout,
                        format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                        level=logging.DEBUG
                        )

    @staticmethod
    def init_app(app):
        pass


class DevelopConfig(Config):
    DEBUG = True
    # MONGO_URI = Config.MONGO_URI_DEV


class ProductConfig(Config):
    # MONGO_URI = Config.MONGO_URI_PROD
    logging.basicConfig(stream=sys.stdout,
                        format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                        level=logging.INFO
                        )


config = {
    'development': DevelopConfig,
    'production': ProductConfig
}
