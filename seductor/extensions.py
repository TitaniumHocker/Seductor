#! -*- coding: utf-8 -*-
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore
from seductor.models import db, User, Role


migrate = Migrate()
security = Security()
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
