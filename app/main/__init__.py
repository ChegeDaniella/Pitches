from flask import Blueprint,Flask
main = Blueprint('main',__name__)
from app.main import views
from flask_bootstrap import Bootstrap

bootstrap= Bootstrap()

def create_app():
    app= Flask(__name__)

    #initializing flask extensions
    bootstrap.init_app(app)

    #Registering the blueprint
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


