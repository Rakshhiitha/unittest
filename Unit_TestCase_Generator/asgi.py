"""
ASGI config for Unit_TestCase_Generator project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

settings_module = 'Unit_TestCase_Generator.deployment_settings' if 'RENDER_EXTERNAL_HOSTNAME' in os.environ else 'Unit_TestCase_Generator.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_asgi_application()
