from flask import Blueprint

main_blueprint = Blueprint('main_blueprint', __name__)

from . import views



# from flask_sqlalchemy import SQLAlchemy

# # Model Class for User
# # Model Class for pitch
# # Model Class for category
# # Model Class for votes
# # Model Class for comments
# db = SQLAlchemy()
# class User(db.Model):
