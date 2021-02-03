import logging
import os

basedir = os.path.abspath(os.path.dirname(__file__))


def build_config(config_object=None):
    environment = os.environ.get('FLASK_ENV')
    logging.info('env '+environment)
    if environment == 'production':
        return ProductionConfig
    elif environment == 'development':
        return DevelopmentConfig
    elif environment == 'testing':
        return TestConfig
    return config_object


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'thisisreallysecretforsure'
    API_CLIENT_ID = os.environ.get('APP_CLIENT_ID')
    API_SECRET_KEY = os.environ.get('API_SECRET_KEY')
    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')


class ProductionConfig(Config):
    DEBUG = False
    EMAIL = True
    LOGGING_CONFIG = 'logging.conf'


class TestConfig(Config):
    LOGIN_DISABLED = False
    PRODUCTION = False
    DEBUG = True
    TEST_DATA = True
    SCHEDULER = False
    LOGGING_CONFIG = 'logging-test.conf'


class DevelopmentConfig(Config):
    LOGIN_DISABLED = False
    DEVELOPMENT = True
    DEBUG = True
    TEST_DATA = True
    SCHEDULER = True
    LOGGING_CONFIG = 'logging.conf'
    # only use for development
    API_ACCESS_TOKEN = 'x9VYCD3vGVH8npqDjXIuLFA3Z0amiQ'
