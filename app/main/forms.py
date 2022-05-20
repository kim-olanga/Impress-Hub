from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField, SubmitField
from wtforms.validators import DataRequired

#User update profile
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Briefly describe yourself.',validators = [DataRequired()])
    submit = SubmitField('Submit')


class PitchesForm(FlaskForm):
    name = StringField('Author Name ', validators=[DataRequired()])
    content = TextAreaField('Enter Your one minute pitch', validators=[DataRequired()])
    
    category = SelectField('Category', choices=[('Health Quote','Health Quote'),('Pick-up' ,'Pick Up Lines'),('Personal Growth','Personal Growth'),('Mum Jokes','Mum Jokes'),('Business','Business')], validators=[DataRequired()])
    submit = SubmitField('Pitch with Impress')

class CommentForm(FlaskForm):
    comment_content = TextAreaField('Provide feedback/Comments', validators=[DataRequired()])
    submit = SubmitField('Add Comment')