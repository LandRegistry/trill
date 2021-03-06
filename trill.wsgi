import os
import sys
import logging
import site

## Path to Python virtual environment
#site.addsitedir('/opt/rh/python33/root/lib/python3.3/site-packages')
site.addsitedir('/var/www/trill/lib/python3.3/site-packages')

logging.basicConfig(stream=sys.stderr)

##Virtualenv Settings
activate_this = '/var/www/trill/bin/activate_this.py'
exec(open(activate_this).read())

##Replace the standard out
sys.stdout = sys.stderr

##Add this file path to sys.path in order to import settings
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..'))

##Add this file path to sys.path in order to import app
sys.path.append('/var/www/trill/')

##Create application for our app
def application(environ, start_response):
    for key in ['TRILL_APPLICATION_URL', 'APPLICATION_SECRET_KEY', 'SQLALCHEMY_DATABASE_URI', 'SETTINGS']:
        os.environ[key] = environ.get(key, '')
    from application.server import app as _application

    return _application(environ, start_response)
