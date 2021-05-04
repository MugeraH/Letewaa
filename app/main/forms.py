from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FormField
from wtforms.validators import DataRequired, Email, Length




class OrderForm(FlaskForm):
    pizza_name = StringField("What type of pizza would you like?", validators=[DataRequired("Please enter a pizza.")])
    time = FormField(TimeForm)
    now_or_later = SelectField("Is your pizza for now or later?", choices=[("NOW", "Now"), ("LATER", "Later")])
    delivery = SelectField("Would you like your pizza delivered or take out?",choices=[("DELIVERY", "Delivery"), ("TAKEOUT", "Take Out")])
    price = SelectField()
    submit = SubmitField("Place Order")
