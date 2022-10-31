from flask import render_template, request, redirect, url_for
from app import apps


from app.models import Customer
from app.prodFunc import getAllProdByID

@apps.route('/')
def homepage():
    product = getAllProdByID()
    return render_template('index.html', product=product)