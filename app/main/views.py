from flask import render_template,request,redirect,url_for,request,redirect,url_for,flash
from . import main
from ..requests import get_weather,get_weather_information,get_days,get_hours,get_minutes
from flask_login import login_required,current_user
from .. import db,photos
from ..email import mail_message
from ..models import Orders,Seller,User,Product,Cart
from .forms import ProductForm,UpdateProfile, UpdateProduct
from ..auth.forms import BuyerRegistrationForm, BuyerLoginForm 
from ..auth2.forms import SellerLoginForm, SellerRegistrationForm


@main.route('/')
def index():
   
    return render_template('index.html')

@main.route('/buyer_login',methods=['GET','POST'])
def login():
    login_form = BuyerLoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

 
    return render_template('auth/login.html',login_form = login_form,)

@main.route('/seller_login',methods=['GET','POST'])
def logintwo():
    login_form = SellerLoginForm()
    if login_form.validate_on_submit():
        seller = Seller.query.filter_by(email = login_form.email.data).first()
        if seller is not None and seller.verify_password(login_form.password.data):
            # login_seller(seller,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.supplier_page'))

        flash('Invalid username or Password')

 
    return render_template('auth2/login.html',login_form = login_form)



@main.route('/buyer_register',methods = ["GET","POST"])
def register():
    form = BuyerRegistrationForm()
    if form.validate_on_submit():
        user =User(email = form.email.data, username = form.username.data,password =form.password.data)
        db.session.add(user)
        db.session.commit()
        
        mail_message("Welcome to Letewaa","email/welcome_user",user.email,user=user)
        
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)


@main.route('/seller_register',methods = ["GET","POST"])
def registertwo():
    form = SellerRegistrationForm()
    if form.validate_on_submit():
        seller =Seller(email = form.email.data, username = form.username.data,password =form.password.data)
        db.session.add(seller)
        db.session.commit()
        
        # mail_message("Welcome to Letewaa","email/welcome_user",seller.email,seller=seller)
        
        return redirect(url_for('auth2.login'))
        title = "New Account"
    return render_template('auth2/register.html',registration_form = form)


@main.route('/user_page')
@login_required
def user_page():
  
    
    supplier_list = Seller.query.all()
    weather_data = get_weather()
   
    weather_icon = get_weather_information(weather_data[0])[0]
    suggestion = get_weather_information(weather_data[0])[1]
   
    return render_template('user/user_page.html',supplier_list=supplier_list,weather_data=weather_data,suggestion=suggestion,weather_icon=weather_icon)

@main.route('/supplier-products/<int:supplier_id>')
@login_required
def supplier_products(supplier_id):
    """
    user supplier id to query suppliers table and get all products of the selected supplier
    button click to add order to cart
    OPTION: have to decide on having an orders form to get user order data

    
    """
    seller = Seller.query.filter_by(id=supplier_id).first()
    product = Product.query.filter_by(id=supplier_id).first()
    
    cart_items = Cart.query.filter_by(user_id=current_user._get_current_object().id).all()
    print(len(cart_items))
    cart_items_count = len(cart_items)
  
  
    supplier_products_list = Product.query.filter_by(seller_id=supplier_id)
   
    return render_template('user/supplier_products.html' ,supplier_products_list=supplier_products_list,seller=seller,cart_items_count=cart_items_count)



@main.route('/add_to_cart/<int:product_id>')
@login_required
def add_to_cart(product_id):
    product = Product.query.filter_by(id=product_id).first()
   
    product_id = product_id
    user_id = current_user
    cart_item = Cart(product_id=product_id,user_id=current_user._get_current_object().id,product= product.product_name,product_picture=product.product_picture)
    cart_item.add_item_to_cart()
    print(cart_item)
    
    return redirect(url_for('.supplier_products', supplier_id = product.seller_id))



@main.route('/checkout')

@login_required
def checkout():
    total_cost=[]
   
    cart_items= Cart.query.filter_by(user_id =current_user._get_current_object().id ).all()
    for item in cart_items:
        total_cost.append(item.product_cost)
        
    total_cost_value= sum(total_cost)
    
    print(total_cost_value)
    
    
   
      
    return render_template('user/checkout.html',cart_items=cart_items,total_cost_value=total_cost_value)

@main.route('/get_cost/<int:product_id>/<int:cartItem_id>',methods=["POST"])
def get_cost(product_id,cartItem_id):
    total_cost=[]
    product = Product.query.filter_by(id=product_id).first()
    cart = Cart.query.filter_by(id=cartItem_id).first()
    cart_items= Cart.query.filter_by(user_id =current_user._get_current_object().id ).all()
    size = request.form.get("size")
    amount = request.form.get("amount")
    
    if size == "large":
        print(size)
        cost = 1000* int(amount)
        cart.product_cost = cost
        cart.amount = amount
        cart.size = size
        db.session.commit()
    elif size == "medium":
        print(size)
        cost = 800* int(amount)
        cart.amount = amount
        cart.size = size
        cart.product_cost = cost
        db.session.commit()
        
    elif size == "small":
        print(size)
        cost = 500* int(amount)
        cart.amount = amount
        cart.size = size
        cart.product_cost = cost
        db.session.commit()
         
    
    return redirect(url_for('.checkout'))



@main.route('/user_confirmation/')
@login_required
def user_confirmation():
    """
    Inform user that their order has been sent and send notification to supplier of a
    new order, also thank the user 
    """
    
    user = User.query.filter_by(id=current_user._get_current_object().id).first()
   
    cart_items= Cart.query.filter_by(user_id =current_user._get_current_object().id ).all()
    
    for item in cart_items:
        product = Product.query.filter_by(id=item.product_id).first()
        order_item_object= Orders(pizza_name=item.product,pizza_size=item.size,price=item.product_cost,user_id=current_user._get_current_object().id ,product_id=item.product_id,seller_id=product.seller_id)
        order_item_object.add_order()
        
        
        
    db.session.query(Cart).delete()
    db.session.commit()
   
   
    return render_template('user/confirmation_page.html',user=user)




# Supplier routes

@main.route('/supplier_page')
@login_required
def supplier_page():
    """
    Supplier is re-directed to their page
    Query orders table by supplier id,and get all active orders
    then click on the orders to go to the orders page

    """
    orders = Orders.query.filter_by(user_id=current_user._get_current_object().id)
   
    return render_template('supplier/supplier_page.html',orders=orders)

@main.route('/orders_page/')
@login_required
def get_orders():
    """
    Get supplier id and use it to query orders db and group by user id/order-id
    """
    orders_list = Orders.query.filter_by(user_id=current_user._get_current_object().id).all()
   
    return render_template('supplier/orders_page.html',orders_list=orders_list)

@main.route('/supplier_confirmation')
@login_required
def supplier_confirmation():
    """
    Supplier notified that he/she has accepted orders and notification has been sent to user
    """
   
    return render_template('supplier_confirmation.html')

@main.route('/update-product/', methods=["GET", "POST"])
# @login_required
def update_products():
   
    """
    Supplier can update their products
    products update form
    add_products where supplier id = current user id
    """
    form = UpdateProduct()
    
    if form.validate_on_submit():
        product_name = form.product_name.data
        description = form.description.data
        filename = photos.save(form.product_picture.data)
        path = f'photos/{filename}'
        seller_id = current_user
        new_product_object = Product(product_name=product_name,description=description,product_picture = path,seller_id=current_user._get_current_object().id)
        
        new_product_object.save_new_product()
        
        
   
    return render_template('supplier/update_product.html',form=form)



#Routes for user profile change
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update_profile.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


#Routes for supplier profile change

@main.route('/supplier/<uname>/update',methods = ['GET','POST'])
@login_required
def update_supplier_profile(uname):
    user = Supplier.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/supplier/<uname>/update/pic',methods= ['POST'])
@login_required
def update_supplier_pic(uname):
    user = Supplier.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
