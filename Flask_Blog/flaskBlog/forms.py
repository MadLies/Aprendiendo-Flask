from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField ,BooleanField
from wtforms.validators import DataRequired , Length ,Email, EqualTo, ValidationError
from flaskBlog.models import User


class RegistrationForm(FlaskForm):
	username =  StringField('Username', validators=[DataRequired(), Length(min = 2 , max= 20)])
	email = StringField('Email', validators=[DataRequired(),Email() ])
	password = PasswordField('Password', validators=[DataRequired() ])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password') ])
	submit = SubmitField('Sing up')

	def validate_username(self, username):
		user = User.query.filter_by(username= username.data).first()
		if user:
			raise ValidationError('This username is taken. Pls change it baby')

	def validate_email(self, email):
		user = User.query.filter_by(email= email.data).first()
		if user:
			raise ValidationError('This email is taken. Pls change it baby')

class LoginForm(FlaskForm):
	
	email = StringField('Email', validators=[DataRequired(),Email() ])
	password = PasswordField('Password', validators=[DataRequired() ])
	remember = BooleanField('Remember Me')
	submit = SubmitField('Login')