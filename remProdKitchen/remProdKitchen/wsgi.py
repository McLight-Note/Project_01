"""
WSGI config for remProdKitchen project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Explicitly set the settings module
os.environ["DJANGO_SETTINGS_MODULE"] = "remProdKitchen.settings"

application = get_wsgi_application()
