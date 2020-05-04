import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dani:4321@localhost/pitches'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("chegedaniella@gmail.com")
    MAIL_PASSWORD = os.environ.get("Angyela2018")

# class TestConfig(Config):
#    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dan:123@localhost/watchlist_test'
class ProdConfig(Config):
    pass  

class DevConfig(Config):
   
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}    

