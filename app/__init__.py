from flask import Flask
from .main.blueprint import main_blueprint 

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)

    return app

if __name__ == '__main__':
    create_app()



# from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import SQLAlchemy

# bootstrap = Bootstrap()
# db = SQLAlchemy()

# def create_app(config_name):
#     app = Flask(__name__)

#     # Initializing flask extensions
#     bootstrap.init_app(app)
#     db.init_app(app)
