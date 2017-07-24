import os

from litego.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

application = get_wsgi_application()
