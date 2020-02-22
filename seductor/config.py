# -*- coding: utf-8 -*-
from os import environ, path

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = environ.get('SECRET_KEY')
API_KEY = environ.get('API_KEY')

SECURITY_PASSWORD_SALT = environ.get('SECURITY_PASSWORD_SALT')
SECURITY_PASSWORD_HASH = environ.get('SECURITY_PASSWORD_HASH')
SECURITY_EMAIL_SENDER = 'no-reply@localhost'

API_ID_SIZE=32

# Domains
# DOMAINS = ['sdct.ru']

# Production database
# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://seductor_user:pass@localhost/seductor_db'

# Devepopment config
SQLALCHEMY_DATABASE_URI = f'sqlite:///{path.join(path.dirname(__file__), path.pardir, "db.sqlite3")}'
DOMAINS = ['localhost:5000']
SCHEME = 'http'
BASE_URL = f'{SCHEME}://{DOMAINS[-1]}'

# logging configuration
LOGGING_LEVEL = 'DEBUG' # DEBUG for developers, ERROR on production
