# -*- coding: utf-8 -*-
from string import ascii_letters, digits
from random import choice
from json import dumps as jsonify
from json import loads as dictify
from datetime import datetime
from ..config import API_ID_SIZE, SCHEME, DOMAINS


BASE_URL = f'{SCHEME}://{DOMAINS[-1]}'

def gen_api_response(data, uri, method, status='success', message=None):
    timestamp = datetime.fromtimestamp(datetime.now().timestamp()).isoformat()
    response = {
            'response': {
                'data': data,
                'request': {
                    'timestamp': timestamp,
                    'id': ''.join(choice(ascii_letters + digits) for _ in range(API_ID_SIZE)),
                    'method': method,
                    'uri': uri
                    },
                'status': status,
                'message': message
                }
            }
    return jsonify(response)

