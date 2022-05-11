import email
from flask import render_template as render, redirect,url_for
from ..models import User
from .forms import RegistrationForm
from .. import db
from flask_login import login_required
from .blueprint import main_blueprint as main

@main.route('/')
def index():
    return render('index.html')

@main.rote('/login', methods=['GET','POST'])
@login_required
def new_review(id):
    pass

@main.route('/register',methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.login'))
        title = "New Account"
    return render('main/register.html',registration_form = form)