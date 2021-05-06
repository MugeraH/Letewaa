from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField,SubmitField, SelectField, FormField,ValidationError
from wtforms.validators import Required, Email, Length
from wtforms import FileField

CATEGORY_CHOICES = [('Large', 'Large'),('Medium', 'Medium'),('Small', 'Small')]


class OrderForm(FlaskForm):
  
    pizza_size = SelectField('Click to select size',choices=CATEGORY_CHOICES,validators=[Required()])
    Amount=StringField("Amount",validators=[Required()])
      
    submit = SubmitField("Add Product",validators=[Required()])
   



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
    description = TextAreaField("Description",validators=[Required()])
    product_picture=FileField("UploadImage",validators=[Required()])
    submit = SubmitField("Place Order",validators=[Required()])
  



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
