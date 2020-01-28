# -*- coding: utf-8 -*-
from flask import render_template
from .blueprint import api
from ..models import *


@api.route('/')
def index():
    return 'test api index page'
