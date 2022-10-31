from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_user, logout_user, current_user
from app.models import Customer, Product, cartTable
from app.prodFunc import getProd

shop = Blueprint('shop', __name__, template_folder='shop_templates')

@shop.route('/product/<int:product_id>')
def showProduct(product_id):
    singleProduct = getProd(product_id)
    return render_template('singleProduct.html', singleProduct=singleProduct)

@shop.route('/cart')
def showCart():
    print(current_user.cust_id)
    print(cartTable.c.cust_id)
    viewCart = Product.query.join(cartTable).join(Customer).filter(cartTable.c.cust_id == current_user.id)
    return render_template('cart.html', viewCart=viewCart)

@shop.route('/add/<int:product_id>')
def addProduct(product_id):
    if Product.query.get(product_id):
        product = Product.query.get(product_id)
        current_user.addToCart(product)
    else:
        product = getProd(product_id)
        name = product['title']
        price = product['price']
        description = product['description']
        category = product['category']
        image = product['image']
        rating = product['rating']
        count = product['count']
        new_product = Product(name, price, description, category, image, rating, count)
        new_product.saveToDB()
        current_user.addToCart(new_product)
        return redirect(url_for('shop.showCart'))
    return redirect(url_for('shop.showCart'))