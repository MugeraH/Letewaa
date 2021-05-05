from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FormField
from wtforms.validators import DataRequired, Email, Length




class OrderForm(FlaskForm):
    pizza_name = StringField("What type of pizza would you like?", validators=[DataRequired("Please enter a pizza.")])
    time = FormField(TimeForm)
    now_or_later = SelectField("Is your pizza for now or later?", choices=[("NOW", "Now"), ("LATER", "Later")])
    price = SelectField("Price")
    pizza size=StringField("size")
    submit = SubmitField("Place Order")
    user_id=StringField("User")
    seller_id=StringField("seller")


class SellerForm(FlaskForm):
    username=StringField("Username")
    email=StringField("Email")
    password=StringField("Password")
    phone=StringField("Contact info")
    profile_picture=StringField("Profile")
    bio=StringField("user bio")
    id=StringField("id")




class ProductForm(FlaskForm):
    product_name = StringField("Name")
    product_description = TextAreaField("Description")
    product_id=StringField("Product")
    product_picture=StringField("Image")
    id=StringField("id")




class UserForm(FlaskForm):
    username=StringField("username")
    email=StringField("email")
    password=StringField("contact info")
    bio=StringField("bio")
    profile_picture=StringField("profile")
    id =StringField("bio")
