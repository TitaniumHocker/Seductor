# -*- cofing: utf-8 -*-
from .app import app as application
from .database import db
from .models import *
from . import views

def get_app():
    return application
