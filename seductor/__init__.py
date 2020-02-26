# -*- coding: utf-8 -*-
from seductor.logger_conf import configuration as log_conf
from seductor.extensions import db, migrate, security
from flask_security import SQLAlchemyUserDatastore
from seductor.models import User, Role
from flask import Flask
import logging.config

# Init Flask application
app = Flask(__name__)
app.config.from_pyfile('config.py')

###
# Init extensions
###
db.init_app(app)  # SQLAlchemy database
migrate.init_app(app, db)  # Migrations
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security.init_app(app, user_datastore)  # Security

# setup logging
logging.config.dictConfig(log_conf)
logger = logging.getLogger('seductor_logger')

from seductor.api import api_bp
app.register_blueprint(api_bp, url_prefix='/api')

from seductor import routes
