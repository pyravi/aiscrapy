import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
#sys.path.append('/home/ubuntu/aiscrapy_website/env/bin/python')
application = get_wsgi_application()

