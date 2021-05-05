from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FormField,ValidationError
from wtforms.validators import DataRequired, Email, Length


CATEGORY_CHOICES = [('Large', 'Large'),('Medium', 'Medium'),('Small', 'Small')]


class OrderForm(FlaskForm):
    # pizza_name = StringField("What type of pizza would you like?", validators=[DataRequired("Please enter a pizza.")])
    pizza size = SelectField('Click to select size',choices=CATEGORY_CHOICES,validators=[Required()])
    Amount=StringField("Amount",validators=[Required()])
      
    submit = SubmitField("Place Order",validators=[Required()])
   



class SellerRegisterForm(FlaskForm):
    username=StringField("Username" ,validators=[Required()])
    email=StringField("Email" ,validators=[Required(),Email()])
    password=StringField("Password" ,validators=[Required()])
    phone=StringField("Contact info" ,validators=[Required()])
    profile_picture=StringField("Profile" ,validators=[Required()])
    bio=StringField("user bio" ,validators=[Required()])
    id=StringField("id" ,validators=[Required()])




class ProductForm(FlaskForm):
    product_name = StringField("Name",validators=[Required()])
    product_description = TextAreaField("Description",validators=[Required()])
    product_id=StringField("Product",validators=[Required()])
    product_picture=FileField("UploadImage",validators=[Required()])
  



