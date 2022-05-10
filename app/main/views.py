from flask import render_template as render
from .blueprint import main_blueprint as main

@main.route('/')
def index():
    return render('index.html')