# -*- coding: utf-8 -*-
from .extensions import db
from datetime import datetime


class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), unique=True, nullable=False)
    created = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    visits = db.Column(db.Integer, default=0, nullable=False)

    def __init__(self, *args, **kwargs):
        super(Links, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'<URL id:{self.id}, original_url:{self.original_url}>'

'''
class Users(db.Model):
    id = db.Column(db.Integer, primaty_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)

    def __init__(self, *args, **kwargs):
        super(Users, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'<User id:{self.id}, name:{self.name}>'
'''
'''
class Visits(db.Model):
    id = db.Column(db.Integer, primaty_key=True)
    date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    link_id = db.Column(db.Integer, )
''' 
