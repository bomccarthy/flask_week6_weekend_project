from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_user, logout_user, current_user
from app.models import Customer, Product
from app.prodFunc import getProd

shop = Blueprint('shop', __name__, template_folder='shop_templates')

@shop.route('/product/<int:product_id>')
def showProduct(product_id):
    singleProduct = getProd(product_id)

    return render_template('singleProduct.html', singleProduct=singleProduct)


@shop.route('/cart')
def showCart():
    

    return render_template('cart.html')

@shop.route('/add/<int:product_id>')
def addProduct(product_id):
    product = getProd(product_id)
    
    current_user.addToCart(product_id)

    return redirect(url_for('showCart'))

