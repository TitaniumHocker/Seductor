#! -*- coding: utf-8 -*-
from .config import LOGGING_LEVEL

configuration = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'stream_format': {
                'format': '{asctime}:{levelname}:{name}:{message}',
                'style': '{'
                }
            },
        'handlers': {
            'stream_handler': {
                'class': 'logging.StreamHandler',
                'level': LOGGING_LEVEL,
                'formatter': 'stream_format'
                }
            },
        'loggers': {
            'seductor_logger': {
                'level': LOGGING_LEVEL,
                'handlers': ['stream_handler']
                }
            }
        }
