from enum import unique
from flask_sqlalchemy import SQLAlchemy
from ..app import db 
# # Model Class for User
# # Model Class for pitch
# # Model Class for category
# # Model Class for votes
# # Model Class for comments
# db = SQLAlchemy()

class User(db.Model):
    __table_name = 'USERS'
    id = db.column(db.Integer, primary_key = True)
    name = db.column(db.string, unique = True)


# from . import db 

# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.column(db.Integer, primary_key = True)
#     username = db.column(db.string(300))

#     def __repr__(self): #makes debugging easier
#         return f'User {self.username}'