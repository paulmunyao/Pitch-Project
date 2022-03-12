
from flask import Flask
app = Flask(__name__)
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app.config.from_object(Config)
db = SQLAlchemy(app)

login = LoginManager(app)
login.login_view = 'login'
from app import models

from .main import main as mainblueprint
app.register_blueprint(mainblueprint,url_prefix='/')
