from flask import Blueprint,Flask
main = Blueprint('main',__name__)
from app.main import views
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap= Bootstrap()

def create_app():
    app= Flask(__name__)

    #initializing flask extensions
    bootstrap.init_app(app)
    login_manager.init_app(app)

    #Registering the blueprint
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


