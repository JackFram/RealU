# default settings
import os


class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = '?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SECURITY_PASSWORD_SALT = 'sadhsajdasdjh!@#s12#S3123'

    # mail config
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # gmail authentication
    MAIL_USERNAME = os.environ['APP_MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['APP_MAIL_PASSWORD']

    # mail accounts
    MAIL_DEFAULT_SENDER = 'realuregister@gmail.com'


class DebugConfig(BaseConfig):
    DEBUG = True


class ProductConfig(BaseConfig):
    DEBUG = False


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
