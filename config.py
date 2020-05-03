import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dani:4321@localhost/pitches'

class TestConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dan:123@localhost/watchlist_test'
class ProdConfig(Config):
    pass  

class DevConfig(Config):
   
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}    

