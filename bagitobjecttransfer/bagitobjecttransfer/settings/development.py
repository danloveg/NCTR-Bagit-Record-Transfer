# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
from pathlib import Path
from .base import *

DEBUG = True
TESTING = False
SITE_ID = 1

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]


# SQLite 3 database is used for development (as opposed to MySQL)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Asynchronous Redis Task Queue Manager
# https://github.com/rq/django-rq

RQ_QUEUES = {
    'default': {
        'HOST': '0.0.0.0',
        'PORT': 6379,
        'DB': 0, # Redis database index
        'PASSWORD': '',
        'DEFAULT_TIMEOUT': 500,
    },
}

if TESTING:
    for queue_config in RQ_QUEUES:
        # Disable aynchronicity if running tests
        queue_config['ASYNC'] = False


# Emailing - Uses MailHog to intercept emails
# MailHog web UI runs at localhost:8025
# More information: https://github.com/mailhog/MailHog

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = '0.0.0.0'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False


# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '{levelname} {asctime} {module}: {message}',
            'style': '{'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO')
        },
        'recordtransfer': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'rq.worker': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}
