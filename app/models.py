from flask_sqlalchemy import SQLAlchemy
from . import db 

# # Model Class for User
# # Model Class for pitch
# # Model Class for category
# # Model Class for votes
# # Model Class for comments
# db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.column(db.Integer, primary_key= True)
    name = db.column(db.string, unique= True)

def __init__(self, name) -> None:
    self.name = name

def __str__(self) -> str:
    return self.name