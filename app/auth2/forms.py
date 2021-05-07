from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, PasswordField, ValidationError,SelectField
from wtforms.validators import Required, Email, EqualTo
from ..models import User, Seller


class SellerRegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
            if Seller.query.filter_by(email = data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if Seller.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class SellerLoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
        
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')


