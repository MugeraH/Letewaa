from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FormField
from wtforms.validators import DataRequired, Email, Length




class OrderForm(FlaskForm):
    pizza_name = StringField("What type of pizza would you like?", validators=[DataRequired("Please enter a pizza.")])
    now_or_later = SelectField("Is your pizza for now or later?", choices=[("NOW", "Now"), ("LATER", "Later")])
    price = SelectField("price")
    submit = SubmitField("Place Order")

class UserForm(FlaskForm):
    username = StringField("name")
    email = StringField("email")
    phone=StringField("Contact info")


class SellerForm(FlaskForm):
    username = StringField("name")
    email=StringField("email")
    phone=StringField("phone")
    


class ProductForm(FlaskForm):    
    product_name = StringField("Name")
    price = StringField("Price")
    description = TextAreaField("Description")   
    