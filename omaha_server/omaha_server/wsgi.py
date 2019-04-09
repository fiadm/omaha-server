"""
WSGI config for omaha_server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "omaha_server.settings_prod")
os.environ.setdefault('UWSGI_PROCESSES', '10')
os.environ.setdefault('UWSGI_THREADS', '8')

from django.core.wsgi import get_wsgi_application
from raven.contrib.django.raven_compat.middleware.wsgi import Sentry

application = Sentry(get_wsgi_application())
