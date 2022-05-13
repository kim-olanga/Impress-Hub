from datetime import datetime

# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import PrimaryKeyConstraint
# from app.main.views import index

from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.column(db.Integer, primary_key= True)
    username = db.column(db.string(300),index= True)
    email = db.column(db.string(300), unique=True)
    password = db.column(db.string(300), nullable=False)
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def set_password(self, password):
        pass_hash = generate_password_hash(password)
        self.password = pass_hash

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'User: {self.username}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Category(db.Model):
    __tablename__='Categories'
    id = db.column(db.Integer, primary_key=True)
    category = db.column(db.string)
    

class Post(db.Model):
    __tablename__='posts'
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

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"Post Title: {self.title}"

class Upvote(db.Model):
    __tablename__='upvotes'
    id = db.column(db.Integer, primary_key = True)
    up_votes = db.column(db.Integer, default=1)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def upvote(cls, id):
        upvote_post = Upvote(user=current_user, post_id=id)
        upvote_post.save()

    @classmethod
    def query_upvotes(cls, id):
        upvote = Upvote.query.filter_by(post_id=id).all()
        return upvote

    @classmethod
    def all_upvotes(cls):
        upvotes = Upvote.query.order_by('id').all()
        return upvotes

    def __repr__(self):
        return f'{self.user_id}:{self.post_id}'

class Downvote(db.Model):
    __tablename__ = 'downvotes'
    id = db.Column(db.Integer, primary_key=True)
    downvote = db.Column(db.Integer, default=1)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def downvote(cls, id):
        downvote_post = Downvote(user=current_user, post_id=id)
        downvote_post.save()

    @classmethod
    def query_downvotes(cls, id):
        downvote = Downvote.query.filter_by(post_id=id).all()
        return downvote

    @classmethod
    def all_downvotes(cls):
        downvote = Downvote.query.order_by('id').all()
        return downvote

    def __repr__(self):
        return f'{self.user_id}:{self.post_id}'

class Comments(db.Model):
    __tablename__='comment'
    id = db.column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    comments = db.column(db.Text())

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls, post_id):
        comment = Comments.query.filter_by(post_id=post_id).all()
        return comment

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'Comments: {self.comment}'