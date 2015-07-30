from flask import Flask
from flask.ext.pagedown import PageDown
from flask.ext.sqlalchemy import SQLAlchemy

# login
import os
from flask.ext.login import LoginManager
from config import basedir

# app
app = Flask(__name__, static_url_path='/static')
app.config.from_object('config')
db = SQLAlchemy(app)
pagedown = PageDown(app)

# login again!
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

# views & models
from app import views, models