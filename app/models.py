from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
import time
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# @login_manager.user_loader
# def load_user(seller_id):
#     return Seller.query.get(int(seller_id))


class User(db.Model,UserMixin):
    __tablename__='users'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String)
    email=db.Column(db.String)
    pass_secure = db.Column(db.String(255))
    phone=db.Column(db.String)
    profile_picture_path=db.Column(db.String)
    orders =db.relationship("Orders", backref="users", lazy="dynamic")
    cart =db.relationship("Cart", backref="users", lazy="dynamic")
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


   
    def __repr__(self):
        return f'User{self.username}'

class Seller(db.Model,UserMixin):
    __tablename__='sellers'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String)
    bio=db.Column(db.String)
    profile_pic_path=db.Column(db.String)
    email=db.Column(db.String)
    pass_secure=db.Column(db.String)
    phone=db.Column(db.String)
    products=db.relationship("Product",backref="sellers", lazy="dynamic")
    orders =db.relationship("Orders", backref="sellers", lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
        


    def __repr__(self):
        return f'Seller{self.username}'
    
    
    

class Product(db.Model):
    __tablename__="products"

    id=db.Column(db.Integer, primary_key=True)
    product_name=db.Column(db.String)
    product_picture=db.Column(db.String)
    description=db.Column(db.String)
    seller_id=db.Column(db.Integer, db.ForeignKey('sellers.id',ondelete='SET NULL'),nullable = True)
    orders=db.relationship("Orders", backref="products", lazy="dynamic")
    cart=db.relationship("Cart", backref="products", lazy="dynamic")
    
    def save_new_product(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Product{self.product}'


class Orders(db.Model):
    __tablename__="orders"

    id=db.Column(db.Integer, primary_key=True)
    pizza_name=db.Column(db.String)
    pizza_size=db.Column(db.String)
    price=db.Column(db.Integer)
    isAccepted=db.Column(db.Boolean,default=False, server_default="false")
    product_id=db.Column(db.Integer, db.ForeignKey('products.id',ondelete='SET NULL'),nullable = True)
    time=db.Column(db.DateTime(),default=datetime.utcnow)
    user_id=db.Column(db.Integer, db.ForeignKey("users.id",ondelete='SET NULL'),nullable = True)
    seller_id=db.Column(db.Integer, db.ForeignKey('sellers.id',ondelete='SET NULL'),nullable = True)
    
    def add_order(self):  
           
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Orders{self.pizza_name}'
    
class Cart(db.Model):
    __tablename__="cart"
    id=db.Column(db.Integer, primary_key=True)
    product=db.Column(db.String)
    product_picture=db.Column(db.String)
    product_price = db.Column(db.Integer)
    amount = db.Column(db.Integer,default=0)
    size=db.Column(db.String)
    product_cost = db.Column(db.Integer,default=0)
    product_id=db.Column(db.Integer, db.ForeignKey('products.id',ondelete='SET NULL'),nullable = True)
    user_id=db.Column(db.Integer, db.ForeignKey("users.id",ondelete='SET NULL'),nullable = True)

    
    def add_item_to_cart(self):      
        db.session.add(self)
        db.session.commit()
     
  
     
    def __repr__(self):
        return f'Cart{self.product}'
    

    
     
    

