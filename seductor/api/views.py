# -*- coding: utf-8 -*-
from flask import render_template
from .blueprint import api
from ..models import *


@api.route('/')
def index():
    return 'You can find API documentation on ...'

@api.route('/link', methods=['GET', 'POST'])
def get_link():
    pass

@api.route('/top', methods=['GET'])
def get_top():
    pass

@api.route('/tkn<token>/link', methods=['GET', 'POST', 'DELETE', 'PUT'])
def auth_link(token):
    pass

# Необязательные параметры: id, время начала, время конца, 
@api.route('/tkn<token>/stat', methods=['POST'])
def auth_stats(token):
    pass


