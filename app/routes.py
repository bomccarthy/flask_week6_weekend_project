from flask import render_template, request, redirect, url_for
from app import apps


from app.models import Customer, Product
from app.prodFunc import getAllProdByID

@apps.route('/')
def homepage():
    product = getAllProdByID()

        # potential_new_product = Product.query.filter_by(prod_id=product).first()

        # if potential_new_product:
        #     return redirect(url_for('/cart')) 

        # else:
        #     new_product = Product(product.id, product.name, product.description, product.price)
        #     new_product.saveToDB()
        #     return redirect(url_for('pokemonCard'))

    return render_template('index.html', product=product)



