#! -*- coding: utf-8 -*-
from flask import request
from flask_restful import Resource, reqparse
from seductor import controller as ctl
from seductor.config import BASE_URL
from seductor.api.tools import generate_api_response as apires
import base62 as b62


parser = reqparse.RequestParser()
parser.add_argument('url', type=str)


class Top(Resource):
    def get(self):
        return apires(
            data=ctl.link.get_top(),
            method=request.method,
            uri=request.path,
        ), 200


class Links(Resource):
    def post(self):
        url = parser.parse_args()['url']
        link = ctl.link.get_by_url(url)
        if link:
            return apires(
                    data={
                        'link': f'{BASE_URL}/{b62.encode(link.id)}'
                        },
                    method=request.method,
                    uri=request.path
                    ), 200
        link = ctl.link.create(url)
        return apires(
                data={
                    'link': f'{BASE_URL}/{b62.encode(link.id)}'
                    },
                method=request.method,
                uri=request.path
                ), 201


class Link(Resource):
    def get(self, id):
        link = ctl.link.get_by_id(id)
        if link:
            return apires(data={
                'id': f'{link.id}',
                'link': f'{BASE_URL}/{b62.encode(link.id)}',
                'original_url': link.original_url
            },
                method=request.method,
                uri=request.path), 200
        else:
            return apires(data=None,
                          method=request.method,
                          uri=request.path,
                          status='fail',
                          message='Link not found'), 404


class Visits(Resource):
    def post(self, link_id):
        pass


class Visit(Resource):
    def get(self, id):
        pass


class Statistic(Resource):
    def get(self, link_id):
        pass
