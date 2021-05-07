from flask import render_template, redirect,url_for,request,flash
from . import auth2
from ..models import Seller,User
from .forms import SellerRegistrationForm,SellerLoginForm
from .. import db
from flask_login import login_user,logout_user,login_required
from ..email import mail_message


@auth2.route('/seller_login',methods=['GET','POST'])
def login():
    login_form = SellerLoginForm()
    if login_form.validate_on_submit():
        seller= Seller.query.filter_by(email = login_form.email.data).first()
        if seller is not None and seller.verify_password(login_form.password.data):
            # login_user(user,login_form.remember.data)
            login_user(seller,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.supplier_page'))

        flash('Invalid username or Password')

 
    return render_template('auth2/login.html',login_form = login_form,)

@auth2.route('/logout')
@login_required
def logout():
    logout_seller()
    return redirect(url_for("main.index"))


@auth2.route('/seller_register',methods = ["GET","POST"])
def register():
    form = SellerRegistrationForm()
    if form.validate_on_submit():
        seller =Seller(email = form.email.data, username = form.username.data,password =form.password.data)
        db.session.add(seller)
        db.session.commit()

        mail_message("Karibu Letewa","email/welcome_seller",seller.email,seller=seller)
        
        return redirect(url_for('auth2.login'))
        title = "New Account"
    return render_template('auth2/register.html',registration_form = form)
