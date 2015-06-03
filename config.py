import os

secret_key = os.environ['APPLICATION_SECRET_KEY']
sqlalchemy_database_uri = os.environ['SQLALCHEMY_DATABASE_URI']

CONFIG_DICT = {
    'DEBUG': False,
    'SECRET_KEY': secret_key,
    'SQLALCHEMY_DATABASE_URI': sqlalchemy_database_uri,
}

settings = os.environ.get('SETTINGS')

if settings == 'development':
    CONFIG_DICT['DEBUG'] = True
elif settings == 'test':
    CONFIG_DICT['DEBUG'] = True
    
# email server
#ip address; mslookup CAS2010
MAIL_SERVER = 'cas2010.diti.lr.net'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USE_SSL = False
#MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
#MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
#MAIL_USERNAME = 'trill.robot@gmail.com'
#MAIL_PASSWORD = 'honeybadger001'

# administrator list
#ADMINS = ['trill.robot@gmail.com']

#class Config(object):
#    DEBUG = False
    # LOGGING_PATH = os.getenv('LOGGING_PATH', 'python_logging/logging.yaml')

#class DevelopmentConfig(Config):
    # format is dialect+driver://username:password@host:port/database
#    SQLALCHEMY_DATABASE_URI = 'postgresql://trill:@0.0.0.0:5432/trill'
#    DEBUG = True

#class UnitTestConfig(Config):
    # Uncomment the line below when the DB is up and running
    #SQLALCHEMY_DATABASE_URI = ''
#    DEBUG = True
