"""
WSGI config for neuralink project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from pathlib import Path
import sys
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'neuralink.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'neuralink.settings')

application = get_wsgi_application()
