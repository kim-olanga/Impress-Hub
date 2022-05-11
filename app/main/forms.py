import email
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField ,SubmitField
from wtforms.validators import Required,Email
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    submit = SubmitField('Sign Up')

from wtforms import ValidationError
class RegistrationForm(FlaskForm):
    # .......
    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    email = StringField('Your Email Adress',validators=[Required(),Email()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')