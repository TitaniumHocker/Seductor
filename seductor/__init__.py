# -*- coding: utf-8 -*-
from seductor.extensions import migrate, security, user_datastore
from seductor.models import db
from seductor.api import api_bp
from seductor.public import public_bp
from flask import Flask
from config import configurations as cfgs
from seductor.exceptions import InvalidConfigurationType
from seductor.logger import set_logger_config


def create_app(mode='development'):
    try:
        cfg = cfgs[mode]
    except KeyError:
        msg = ('Unknown config type, use "production",'
               ' "development" or "testing"')
        raise InvalidConfigurationType(msg)

    app = Flask(__name__)
    app.config.from_object(cfg)

    set_logger_config(level=app.config.get('LOGGING_LEVEL', 'ERROR'))

    db.init_app(app)  # SQLAlchemy database
    migrate.init_app(app, db)  # Migrations
    security.init_app(app, user_datastore)  # Security

    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(public_bp, url_prefix='/')

    return app
