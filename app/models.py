from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint
from . import db 
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.column(db.Integer, primary_key=True)
    username = db.column(db.string(300))
    email = db.column(db.string(300), unique=True)

    def __repr__(self): 
       return f'User Name{self.username}'

class Category(db.Model):
    __tablename__='Categories'
    id = db.column(db.Integer, primary_key=True)
    category = db.column(db.string)
    

class Pitches(db.Model):
    __tablename__='pitch'
    id = db.column(db.Integer, Primary_Key=True)
    title = db.column(db.string, nullable=False)
    body = db.column(db.Text, nullable= False)
    user_id = db.column(db.Integer, db.ForeignKey('users.id')) 
    user = db.relationship(User, backref=db.backref('pitches', lazy=True))
    category = db.column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship(Category, backref=db.backref('pitches', lazy=False))
    votes = db.column(db.Integer, db.ForeignKey('votes.id'))
    votes = db.relationship('Votes', backref=db.backref('pitches', lazy=True))
    comments_id = db.column(db.Integer, db.ForeignKey('comments.id'))
    comments_id = db.relationship('Comments', backref=db.backref('pitches', lazy=True))

class Votes(db.Model):
    __tablename__='vote'
    id = db.column(db.Integer, primary_key = True)
    down_votes = db.column(db.Integer)
    up_votes = db.column(db.Integer)

class Comments(db.Model):
    __tablename__='comment'
    id = db.column(db.Integer, primary_key=True)
    comments = db.column(db.string)