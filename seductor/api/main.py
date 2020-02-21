#! -*- coding: utf-8 -*-
from flask_restful import Api
from .blueprint import api_bp
from .resources import Links, Link


api = Api(api_bp)
api.add_resource(Links, '/links')
api.add_resource(Link, '/links/<link_id>')
