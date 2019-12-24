# -*- coding: utf-8 -*-
from flask import request, render_template, redirect, abort
from .app import app
from .extensions import db
from .models import Links
import base62


@app.route('/', methods=['GET', 'POST'])
def index_page():
    return render_template('index.html')


@app.route('/about', methods=['GET', 'POST'])
def about_page():
    return render_template('about.html')


@app.route('/top', methods=['GET', 'POST'])
def top_page():
    return render_template('top.html')


@app.errorhandler(404)
def not_found_page(e):
    return render_template('404.html'), 404
