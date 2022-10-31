from flask import render_template, request, redirect, url_for
from app import apps


from app.models import Customer, Product
from app.prodFunc import getAllProdByID

@apps.route('/')
def homepage():
    product = getAllProdByID()
    return render_template('index.html', product=product)

@apps.route('/search')
def search():
    product = getAllProdByID()
    return render_template('search.html', product=product)