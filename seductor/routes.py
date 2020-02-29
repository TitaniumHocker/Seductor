# -*- coding: utf-8 -*-
from flask import request, render_template, redirect, abort
import seductor.controller as ctl
from seductor import app
from seductor.config import BASE_URL
import base62 as b62


@app.route('/', methods=['GET', 'POST'])
def index_page():
    if request.method == 'GET':
        return render_template('index.html')
    url = request.form.get('url')
    link = ctl.link.get_by_url(url)
    if link:
        short_url = f'{BASE_URL}/{b62.encode(link.id)}'
        return render_template('magic.html',
                               short_url=short_url,
                               qrname=b62.encode(link.id))
    link = ctl.link.create(url)
    short_url = f'{BASE_URL}/{b62.encode(link.id)}'
    return render_template('magic.html',
                           short_url=short_url,
                           qrname=b62.encode(link.id)), 201


@app.route('/about', methods=['GET'])
def about_page():
    return render_template('about.html')


@app.route('/stats', methods=['GET'])
def top_page():
    top = ctl.link.get_top()
    return render_template('stats.html', top=top)


@app.route('/<link_id>')
def redirect_link(link_id):
    link = ctl.link.get_by_id(b62.decode(link_id))
    if not link:
        abort(404)
    ctl.link.register_visit(link, request.remote_addr)
    return redirect(link.original_url)
