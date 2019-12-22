# -*- coding: utf-8 -*-
from os import environ

SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = environ.get('SECRET_KEY')
API_KEY = environ.get('API_KEY')

# Domains
# DOMAINS = ['sdct.ru']

# Production database
# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://seductor_user:pass@localhost/seductor_db'

# Devepopment config
SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
DOMAINS = ['localhost']

