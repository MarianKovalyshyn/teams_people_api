import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'teams_people_api.settings')

application = get_asgi_application()
