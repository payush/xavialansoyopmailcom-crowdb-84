"""
WSGI config for xavialansoyopmailcom_crowdb_84 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xavialansoyopmailcom_crowdb_84.settings")

application = get_wsgi_application()
