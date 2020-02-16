# -*- coding: utf-8 -*-
from os import environ, path

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = environ.get('SECRET_KEY')
API_KEY = environ.get('API_KEY')

API_ID_SIZE=16

# Domains
# DOMAINS = ['sdct.ru']

# Production database
# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://seductor_user:pass@localhost/seductor_db'

# Devepopment config
SQLALCHEMY_DATABASE_URI = f'sqlite:///{path.join(path.dirname(__file__), path.pardir, "db.sqlite")}'
DOMAINS = ['localhost:5000']
SCHEME = 'http'
