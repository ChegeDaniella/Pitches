import os

class Config:
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dani:4321@localhost/pitches'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATION= True
    
    #  email configurations
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIl_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass

class TestConfig(Config):
    DATABASE_PASS=os.environ.get('DATABASE_PASS')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dani:4321@localhost/pitches_test'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dani:4321@localhost/pitches'
   
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
} 