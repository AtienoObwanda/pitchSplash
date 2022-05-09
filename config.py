import os

class Config:
    '''
    Parent config class
    '''
    SECRET_KEY =os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    # Mail confugurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS=True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SUBJECT_PREFIX = 'PITCH SPLASH!'
    SENDER_EMAIL = 'splashpitch@gmail.com'
    # MAIL_PASSWORD = 'afSG7AyE123clear'
    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
uri = os.getenv('DATABASE_URL')
if uri and uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)
        
SQLALCHEMY_DATABASE_URI=uri

class TestConfig(Config):
    '''
    Test
    '''
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig,
}
