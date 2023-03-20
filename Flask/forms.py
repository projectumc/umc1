from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class Registrationform(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    
    age = StringField('Age',
                           validators=[DataRequired(), Length(min=2, max=20)])
    
    # cant leave empty, and only 2-20 character
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[
                                     DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    


class Loginform(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('log In')
        
    # Now when we use these forms we need to use a secret keys for our application, a secret key will help us against modifying cookies and cross-site request forgery attacks and tings like that
