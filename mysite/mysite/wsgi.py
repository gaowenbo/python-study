"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
from django.utils.deprecation import MiddlewareMixin
from django.middleware.csrf import get_token


class CsrfTokenMiddleware(MiddlewareMixin):
    def process_request(self, request):
        get_token(request)

application = get_wsgi_application()
