from flask.ext.wtf import Form
from wtforms import TextAreaField, StringField, BooleanField
from wtforms.validators import DataRequired
from flask.ext.pagedown.fields import PageDownField

class LoginForm(Form):
	username = StringField('username', validators=[DataRequired()])
	password = StringField('password', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)

class PostForm(Form):
	post = TextAreaField('post', validators=[DataRequired()])

class PageDownForm(Form):
	post = PageDownField('Enter your markdown blog post.', validators=[DataRequired()])
