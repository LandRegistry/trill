import os

class Config(object):
    DEBUG = False
    # LOGGING_PATH = os.getenv('LOGGING_PATH', 'python_logging/logging.yaml')

class DevelopmentConfig(Config):
    # format is dialect+driver://username:password@host:port/database
    # Uncomment the line below when the DB is up and running
    #SQLALCHEMY_DATABASE_URI = 'postgresql://trill:trill@localhost/trill'
    DEBUG = True

class UnitTestConfig(Config):
    # Uncomment the line below when the DB is up and running
    SQLALCHEMY_DATABASE_URI = ''
    DEBUG = True

    basedir = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = 'postgresql://trill:@0.0.0.0:5432/trill'
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
