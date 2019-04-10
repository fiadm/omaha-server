import os

from .settings_default import *

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
PUBLIC_READ_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
STATIC_URL = '/static/'

HOST_NAME = '206.54.191.7'
OMAHA_URL_PREFIX = 'http://206.54.191.7'
