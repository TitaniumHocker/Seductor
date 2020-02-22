#! -*- coding: utf-8 -*-
from flask import Blueprint
from seductor.api.extensions import api
from seductor.api.resources import Top, Links, Link


api_bp = Blueprint('api', __name__)
api.init_app(api_bp)

api.add_resource(Links, '/links')
api.add_resource(Link, '/links/<id>')
api.add_resource(Top, '/top')
