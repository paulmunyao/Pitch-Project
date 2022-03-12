from app import app, db
from flask import render_template, flash, redirect, url_for
from app.main.forms import LoginForm, RegistrationForm,PostForm
from flask_login import current_user, login_required, logout_user, login_user
from app.models import User, Post
from flask import request
from werkzeug.urls import url_parse


@app.route('/')
def index():
    blogs = Post.query.all()
    user = {"username": "WELCOME TO THE DEN"}
    posts = {"Welcome to the den where powerful ideas are shared and if you're not prepared one can be eaten or as they say the hunter becomes the hunted"}
    return render_template('index.html', title='Home', user=user, posts=posts,blogs=blogs)


@app.route('/Login', methods=['GET', 'POST'])
def Login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.password_hash==form.password.data:
            flash('Invalid username or password')
            return redirect(url_for('Login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
        flash('Login requested for user {},remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('Login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data,password_hash=form.password.data)
        # user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('Login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'title': user, 'description': 'Test post #1'},
    ]
    return render_template('user.html', user=user, posts=posts)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/posts', methods=['GET', 'POST'])
def publish():
    form = PostForm()
    if form.validate_on_submit():
        post_create = Post(title=form.title.data,description=form.description.data)
        db.session.add(post_create)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('post.html',form=form)
