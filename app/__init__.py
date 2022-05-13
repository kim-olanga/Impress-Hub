from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from config import config_options
# from flask_migrate import Migrate
# from .main import main_blueprint 

app = Flask(__name__)

db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap()
mail = Mail(app)
# migrate = Migrate()
login_manager.login_view = 'auth.login'
login_manager.session_protection = 'strong'

def create_app(config_name):
    app.config.from_object(config_options[config_name])
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
    return app

# if __name__ == '__main__':
    # load_dotenv(find_dotenv())
    # create_app()