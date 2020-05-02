import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:password@localhost/pitches'

class ProdConfig(Config):
    pass  

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dan:123@localhost/watchlists'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}    

