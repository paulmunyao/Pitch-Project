import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    FLASK_ENV='development'
    SECRET_KEY = 'guess-me'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
