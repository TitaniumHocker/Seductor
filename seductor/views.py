# -*- coding: utf-8 -*-
from flask import request, render_template, redirect, abort, url_for
from .app import app
from .extensions import db
from .models import Links
import base62

# Redirection filter regex sample
# ^http(s)?:\/\/(www\.)?(sdct\.ru|seductor\.ru)(\/.+|\/)?$
BASE_URL = f'{app.config["SCHEME"]}://{app.config["DOMAINS"][-1]}'

@app.route('/', methods=['GET', 'POST'])
def index_page():
    if request.method == 'GET':
        return render_template('index.html')

    url = request.form.get('url')
    query = Links.query.filter_by(original_url=url).first()
    if query:
        short_url = f'{BASE_URL}/{base62.encode(query.id)}'
        return render_template('magic.html', short_url=short_url)

    link = Links(original_url=url)
    db.session.add(link)
    db.session.commit()
    db.session.refresh(link)
    short_url = f'{BASE_URL}/{base62.encode(link.id)}'
    return render_template('magic.html', short_url=short_url), 201

@app.route('/<magical_url>')
def magical_page(magical_url):
    link = Links.query.filter_by(id=base62.decode(magical_url)).first_or_404()
    link.visits += 1
    db.session.commit()
    return redirect(link.original_url)

@app.route('/about', methods=['GET', 'POST'])
def about_page():
    return render_template('about.html')


@app.route('/top', methods=['GET', 'POST'])
def top_page():
    return render_template('top.html')

@app.errorhandler(404)
def not_found_page(e):
    return render_template('404.html'), 404
