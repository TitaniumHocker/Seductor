#! -*- coding: utf-8 -*-
import logging.config


def set_logger_config(level='DEBUG'):
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
                'level': level,
                'formatter': 'stream_format'
            }
        },
        'loggers': {
            'seductor_logger': {
                'level': level,
                'handlers': ['stream_handler']
            }
        }
    }

    logging.config.dictConfig(configuration)
    return


logger = logging.getLogger('seductor_logger')
