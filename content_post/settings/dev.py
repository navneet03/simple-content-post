from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_WHITELIST = (
    '*',
)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e#(tm_ujycogs-npr*1cmz-3^^@owb*dm5i-lt613y@wy_fb8w'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
