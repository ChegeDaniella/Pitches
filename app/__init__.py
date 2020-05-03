from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options

db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):
    # Initializing application
    app = Flask(__name__)

    #creating app configurations
    app.config.from_object(config_options[config_name])
    

    # Initializing Flask Extensions
    bootstrap = Bootstrap(app)
    db.init_app(app)
    
    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app