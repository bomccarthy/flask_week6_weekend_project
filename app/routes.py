from app import app
from flask import render_template, request, redirect, url_for


from app.models import Customer
import app.prodFunc

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')
