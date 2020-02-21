#! -*- coding: utf-8 -*-
from flask import request
from flask_restful import Resource
from .. import controller as ctl
from ..config import BASE_URL
from .tools import generate_api_response as gapir
import base62 as b62


class Links(Resource):
    def post(self, url):
        if link := ctl.link.get_by_url(url):
            return gapir(
                    data={
                        'link': f'{BASE_URL}/{b62.encode(link.id)}'
                        },
                    method=request.method,
                    uri=request.path
                    ), 200
        link = ctl.link.create(url)
        return gapir(
                data={
                    'link': f'{BASE_URL}/{b62.encode(link.id)}'
                    },
                method=request.method,
                uri=request.path
                ), 201


class Link(Resource):
    def get(self, id):
        if link := ctl.link.get_by_id(id):
            return gapir(
                    data={
                        'id': f'{link.id}',
                        'link': f'{BASE_URL}/{b62.encode(link.id)}',
                        'original_url': link.original_url
                        },
                    method=request.method,
                    uri=request.path
                    ), 200
        return gapir(
                data=None,
                method=request.method,
                uri=request.path,
                status='fail',
                message='Link not found'
                ), 404


class Visits(Resource):
    def post(self, link_id, remote_addr, user_agent):
        pass


class Visit(Resource):
    def get(self, id):
        pass

    def post(self, link_id):
        pass


class Statistic(Resource):
    def get(self, link_id):
        pass
