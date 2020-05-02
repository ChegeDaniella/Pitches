from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app():
    # Initializing application
    app = Flask(__name__)

    # Initializing Flask Extensions
    bootstrap = Bootstrap(app)

    # from app import views

    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app