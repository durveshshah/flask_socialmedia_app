from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Leng	th(min = 2,max = 20)])

	email = StringField('Email',validators = [DataRequired(), Email()])

	password = PasswordField('Password',validators = [DataRequired()])

	confirm_password = PasswordField('Confirm Password',validators = [DataRequired(),EqualTo('password')])

	submit = SubmitField('Sign Up')

	# Function to validate username if it already exists
	def validate_username(self,username):
		user = User.query.filter_by(username = username.data).first()

		if user:
			raise ValidationError('Username already exists. Please choose a different username')


    # Function to validate email if it already exists
	def validate_email(self,email):
		user = User.query.filter_by(email = email.data).first()

		if user:
			raise ValidationError('Email already exists. Please choose a different Email')			

class LoginForm(FlaskForm):

	email = StringField('Email',validators = [DataRequired(), Email()])

	password = PasswordField('Password',validators = [DataRequired()])

	remember = BooleanField('Remember Me')

	submit = SubmitField('Log In')