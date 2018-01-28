from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['localhost']

CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
    'localhost',
)
