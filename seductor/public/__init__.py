#! -*- coding: utf-8 -*-
from flask import Blueprint


public_bp = Blueprint('public', __name__)


from seductor.public import routes
