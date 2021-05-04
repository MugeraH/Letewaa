from . import db
from datetime import datetime


class User(db.Model):
    __tablename__='users'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String)
    email=db.Column(db.String)
    password=db.Column(db.String)
    phone=db.Column(db.String)
    bio=db.Column(db.String)
    profile_picture=db.Column(db.String)
    user=db.relationship("Orders", backref="users", lazy="dynamic")


    def __repr__(self):
        return f'User{self.username}'

class Seller(db.Model):
    __tablename__='sellers'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String)
    bio=db.Column(db.String)
    profile_picture=db.Column(db.String)
    email=db.Column(db.String)
    password=db.Column(db.String)
    phone=db.Column(db.String)
    products=db.relationship("Product",backref="sellers", lazy="dynamic")
    sellers=db.relationship("Orders", backref="sellers", lazy="dynamic")

    def __repr__(self):
        return f'Seller{self.username}'

class Product(db.Model):
    __tablename__="products"

    id=db.Column(db.Integer, primary_key=True)
    product_name=db.Column(db.String)
    product_picture=db.Column(db.String)
    description=db.Column(db.String)
    seller_id=db.Column(db.Integer, db.ForeignKey('sellers.id'))
    orders=db.relationship("Orders", backref="products", lazy="dynamic")

    def __repr__(self):
        return f'Product{self.product}'

class Orders(db.Model):
    __tablename__="orders"

    id=db.Column(db.Integer, primary_key=True)
    pizza_name=db.Column(db.String)
    pizza_size=db.Column(db.String)
    price=db.Column(db.Integer)
    product_id=db.Column(db.Integer, db.ForeignKey('products.id'))
    time=db.Column(db.DateTime(),default=datetime.utcnow)
    user_id=db.Column(db.Integer, db.ForeignKey("users.id"))
    seller_id=db.Column(db.Integer, db.ForeignKey('sellers.id'))

    def __repr__(self):
        return f'Orders{self.pizza_name}'
    

