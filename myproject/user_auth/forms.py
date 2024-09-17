from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email,EqualTo, InputRequired

class RegisterForm(FlaskForm):

    username = StringField('Username', validators=[InputRequired()], render_kw={'placeholder': 'Username', 'class':'form-control'})
    email = StringField('Email', validators=[InputRequired(),Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    pass_confirm = PasswordField('Confirm Password', validators=[InputRequired(),EqualTo('password',message='Passwords must match')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):

    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Log In')