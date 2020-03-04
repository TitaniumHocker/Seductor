# -*- coding: utf-8 -*-
from os import environ, path
import tempfile


class BasicConfig():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = environ.get('SECRET_KEY')
    API_KEY = environ.get('API_KEY')
    SECURITY_PASSWORD_SALT = environ.get('SECURITY_PASSWORD_SALT')
    SECURITY_PASSWORD_HASH = environ.get('SECURITY_PASSWORD_HASH')
    API_ID_SIZE = 32
    LINK_PREFIX = 'l'
    QR_CODE_PREFIX = 'q'


class DevelepmentConfig(BasicConfig):
    SECURITY_EMAIL_SENDER = 'no-reply@localhost'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{path.join(path.dirname(__file__), "db.sqlite3")}'
    DOMAINS = ['localhost:5000']
    SCHEME = 'http'
    LOGGING_LEVEL = 'DEBUG'
    BASE_URL = f'{SCHEME}://{DOMAINS[-1]}'


class ProductionConfig(BasicConfig):
    SECURITY_EMAIL_SENDER = 'noreply@sdct.ru'
    DOMAINS = ['sdct.ru']
    SCHEME = 'http'
    BASE_URL = f'{SCHEME}://{DOMAINS[-1]}'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://seductor_user:pass@localhost/seductor_db'
    LOGGING_LEVEL = 'ERROR'


class TestingConfig(DevelepmentConfig):
    SECURITY_EMAIL_SENDER = 'noreply-test@localhost'
    TESTING = True


configurations = {
    'production': ProductionConfig,
    'development': DevelepmentConfig,
    'testing': TestingConfig
}
