# -*- coding: utf-8 -*-
from flask_security import UserMixin, RoleMixin
from datetime import datetime
from seductor.extensions import db


roles_users = db.Table('roles_users',
                       db.Column('user_id',
                                 db.Integer,
                                 db.ForeignKey('users.id')),
                       db.Column('role_id',
                                 db.Integer,
                                 db.ForeignKey('roles.id'))
                       )


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, nullable=False)
    username = db.Column(db.String(32), unique=True, nullable=True)
    password = db.Column(db.String(256), nullable=False)
    active = db.Column(db.Boolean)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    links = db.relationship('Link', backref=db.backref('owner'))


class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)


class Link(db.Model):
    __tablename__ = 'links'
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2048), unique=True, nullable=False)
    created = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    visits = db.relationship('Visit', backref='link', lazy='dynamic')
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, *args, **kwargs):
        super(Link, self).__init__(*args, **kwargs)

    def __repr__(self):
        return (f'<Link id:{self.id}, '
                f'created:{self.created}, '
                f'original_url:{self.original_url}>')


class Visit(db.Model):
    __tablename__ = 'visits'
    id = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String(40), nullable=True)
    created = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    link_id = db.Column(db.Integer, db.ForeignKey('links.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        super(Visit, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'Visit id:{self.id}, created:{self.created}, host:{self.host}>'
