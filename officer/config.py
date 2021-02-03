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
    API_CLIENT_ID = 'ecwgleloykidsc9v2d6gajg5'
    API_SECRET_KEY = '9zudg0xblrzcav6bhn0lewdwz'
    GOOGLE_CLIENT_ID = '175325454822-pe6ndus00851osas8v8'\
        'd5ofdkeqdh7a1.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = 'TC-2DcVjUaJpfQncrCKa16dU'


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
