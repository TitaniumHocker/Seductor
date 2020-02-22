#! -*- coding: utf-8 -*-
from datetime import datetime
# from json import dumps as jsonify
from string import ascii_letters, digits
from random import choice
from seductor.config import API_ID_SIZE


def generate_api_response(data, method, uri, status='success', message=None):
    timestamp = datetime.fromtimestamp(datetime.now().timestamp()).isoformat()
    response_id = ''.join(choice(ascii_letters + digits)
                          for _ in range(API_ID_SIZE))
    response = {
            'data': data,
            'request': {
                'timestamp': timestamp,
                'id': response_id,
                'method': method,
                'uri': uri
                },
            'status': status,
            'message': message
            }
    return response
