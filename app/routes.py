from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {"username": "WELCOME TO THE DEN"}
    posts = {"Welcome to the den where powerful ideas are shared and if you're not prepared one can be eaten or as they say the hunter becomes the hunted"}
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)   