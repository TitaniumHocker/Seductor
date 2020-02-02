# -*- coding: utf-8 -*-
from flask import Response, redirect, url_for, request, abort
from json import loads as dictify
from json import dumps as jsonify
from .extensions import gen_api_response, BASE_URL
from .blueprint import api
from ..extensions import db
from ..models import *
import base62


# Response(gen_api_response('', '/', 'GET'), mimetype='application/json')
@api.route('/', methods=['GET'])
def index():
    return redirect('http://docs.sdct.ru/')

@api.route('/link', methods=['POST'])
def get_link():
    try:
        url = request.get_json()['url']
    except KeyError:
        abort(400)
    query = Links.query.filter_by(original_url=url).first()
    if query:
        short_url = f'{BASE_URL}/{base62.encode(query.id)}'
        resp = gen_api_response(
                {'magic_url': short_url},
                request.path,
                request.method,
                message='Found'
                )
        return Response(resp, mimetype='application/json'), 200
    link = Links(original_url=url)
    db.session.add(link)
    db.session.commit()
    db.session.refresh(link)
    short_url = f'{BASE_URL}/{base62.encode(link.id)}'
    resp = gen_api_response(
            jsonify({'magic_url': short_url}),
            request.path,
            request.method,
            message='Created'
            )
    return Response(resp, mimetype='application/json'), 201

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


