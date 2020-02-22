#! -*- coding: utf-8 -*-

# SQL Alchemy | Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Migrations | Flask-Migrate
from flask_migrate import Migrate
migrate = Migrate()

# security | Flask-Security
from flask_security import Security
security = Security()
