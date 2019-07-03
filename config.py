import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG =False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'alexkorirkipkoech1993'

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT =True
    DEBUG = True

class DevelopmentConfig(config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(config):
    TESTING = True