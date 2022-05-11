import os
from dotenv import load_dotenv,find_dotenv
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .main.blueprint import main_blueprint 

bootstrap = Bootstrap()
db = SQLAlchemy()
from app import models
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    db.init_app(app)
    migrate.init_app(app, db)

    return app

if __name__ == '__main__':
    load_dotenv(find_dotenv())
    create_app()