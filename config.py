import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATION= True
    
    
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_USE_SSL = True
    
     # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    # @staticmethod
    # def init_app(app):
    #     pass

# class TestConfig(Config):
#     # DATABASE_PASS=os.environ.get('DATABASE_PASS')
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dani:4321@localhost/pitches_test'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    # SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dany:4321@localhost/pitch'
   
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
} 