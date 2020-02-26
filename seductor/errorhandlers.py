#! -*- coding: utf-8 -*-
from flask import render_template
from seductor import app


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404
