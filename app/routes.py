from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask import login_required
from flask import request
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm


@app.route('/')
@app.route('/index')
def index():
    user = {"username": "WELCOME TO THE DEN"}
    posts = {"Welcome to the den where powerful ideas are shared and if you're not prepared one can be eaten or as they say the hunter becomes the hunted"}
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET' 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Inavlid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
        flash('Login requested for user {},remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/')
@app.route('/index')
def index():
    user = {"username": "WELCOME TO THE DEN"}
    posts = {"Welcome to the den where powerful ideas are shared and if you're not prepared one can be eaten or as they say the hunter becomes the hunted"}
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'title': user, 'description': 'Test post #1'},
    ]
    return render_template('user.html', user=user, posts=posts)
