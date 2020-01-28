# -*- coding: utf-8 -*-

from .blueprint import api as api_blueprint
from . import views

def get_api_blueprint():
    return api_blueprint
