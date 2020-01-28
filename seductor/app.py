# -*- coding: utf-8 -*-
from flask import Flask
from .extensions import db
from . import api


app = Flask(__name__)
app.config.from_pyfile('config.py')
app.register_blueprint(api.api_blueprint, url_prefix='/api')
db.init_app(app)

