# -*- coding: utf-8 -*-
from flask import Flask
from .logger_conf import configuration as log_conf
import logging.config
from flask_migrate import Migrate
from flask_security import (
        Security, SQLAlchemyUserDatastore
        )
from .database import db
from .models import User, Role


app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

# setup logging
logging.config.dictConfig(log_conf)
logger = logging.getLogger('seductor_logger')

# set migrate for flask db CLI interface
migrate = Migrate(app, db)

# setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
