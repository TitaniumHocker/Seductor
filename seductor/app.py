# -*- coding: utf-8 -*-
from flask import Flask
from flask_migrate import Migrate
from .database import db


app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)


# set migrate for flask db CLI interface
migrate = Migrate(app, db)

