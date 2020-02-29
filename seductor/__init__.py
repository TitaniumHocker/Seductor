# -*- coding: utf-8 -*-
from seductor.extensions import migrate, security, user_datastore
from seductor.models import db
from seductor.api import api_bp
from flask import Flask


app = Flask(__name__)
app.config.from_pyfile('config.py')

db.init_app(app)  # SQLAlchemy database
migrate.init_app(app, db)  # Migrations
security.init_app(app, user_datastore)  # Security

app.register_blueprint(api_bp, url_prefix='/api')


def create_app():
    return app


from seductor import routes, errorhandlers
