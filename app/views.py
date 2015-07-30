from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, lm
from .forms import LoginForm, PostForm, PageDownForm
from .models import User
from datetime import datetime

@app.before_request
def before_request():
	g.user = current_user

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	return render_template('index.html',
													title='Home')

@app.route('/blog', methods=['GET', 'POST'])
def blog():
	form = PostForm()
	return render_template('blog.html',
													title='Blog',
													form=form)
													#posts=posts)

@lm.user_loader
def load_user(id):
	return User.get(id)

@app.route('/login', methods=['GET', 'POST'])
def login():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('blog'))
	form = LoginForm()
	if form.validate_on_submit():
		session['remember_me'] = form.remember_me.data
	return render_template('login.html',
													title='Sign In',
													form=form)

@app.route('/login/check', methods=['POST'])
def login_check():
	form = LoginForm()
	user = User.get(request.form['username'])
	if (user and user.password == request.form['password']):
		login_user(user)
		return redirect(url_for('blog'))
	else:
		flash('Incorrect username or password.')
		return redirect(url_for('login'))

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('blog'))

#@app.errorhandler(403)
#def UserNotFoundError(error):
#	return redirect(url_for('blog')), 403
#	flash('User not found.')

@app.route('/gallery')
def gallery():
	return render_template('gallery.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/portfolio')
def portfolio():
	return render_template('portfolio.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')



