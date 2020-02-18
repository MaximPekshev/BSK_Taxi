# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u0872810/data/www/taxi.bsk31.com/BSK_Taxi')
sys.path.insert(1, '/var/www/u0872810/data/djenvtaxi/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'BSK_Taxi.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()