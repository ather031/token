import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sms.settings')
os.environ.setdefault('HTTPS', 'on')
django.setup()

from django.urls import re_path,path
from django.core.asgi import get_asgi_application
application = ProtocolTypeRouter(
    {
        "https": get_asgi_application(),
    }
)