# -*- coding: utf-8 -*-
from flask import request, render_template, redirect, abort
import seductor.controller as ctl
from flask import current_app as app
from seductor.public import public_bp as bp
import base62 as b62


@bp.route('/', methods=['GET', 'POST'])
def index_page():
    if request.method == 'GET':
        return render_template('index.html')
    url = request.form.get('url')
    link = ctl.link.get_by_url(url)
    if link:
        short_url = (f'{app.config.get("BASE_URL")}/'
                     f'{app.config.get("LINK_PREFIX")}'
                     f'{b62.encode(link.id)}')
        qr_name = f'{app.config.get("QR_CODE_PREFIX")}{b62.encode(link.id)}'
        return render_template('magic.html',
                               short_url=short_url,
                               qr_name=qr_name)
    link = ctl.link.create(url)
    short_url = (f'{app.config.get("BASE_URL")}/'
                 f'{app.config.get("LINK_PREFIX")}'
                 f'{b62.encode(link.id)}')
    qr_name = f'{app.config.get("QR_CODE_PREFIX")}{b62.encode(link.id)}'
    return render_template('magic.html',
                           short_url=short_url,
                           qr_name=qr_name), 201


@bp.route('/about', methods=['GET'])
def about_page():
    return render_template('about.html')


@bp.route('/stats', methods=['GET'])
def top_page():
    top = ctl.link.get_top()
    return render_template('stats.html', top=top)


@bp.route('/l<link_id>')
def redirect_link(link_id):
    link = ctl.link.get_by_id(b62.decode(link_id))
    if not link:
        abort(404)
    ctl.link.register_visit(link, request.remote_addr)
    return redirect(link.original_url)
