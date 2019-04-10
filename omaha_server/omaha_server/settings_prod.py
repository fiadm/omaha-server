import os

from .settings_default import *

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
PUBLIC_READ_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

HOST_NAME = '206.54.191.7'
OMAHA_URL_PREFIX = 'http://{}'.format(HOST_NAME)

STATIC_URL = '{}/static/'.format(OMAHA_URL_PREFIX)
MEDIA_URL = '{}/static/media/'.format(OMAHA_URL_PREFIX)

CUP_REQUEST_VALIDATION = True
CUP_PEM_KEYS = {
    '9': '/srv/omaha/deploy/cup_private.pem'
}
