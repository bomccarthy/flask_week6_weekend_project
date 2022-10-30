from flask import render_template, request, redirect, url_for
from app import app

from app.models import Customer
import app.prodFunc

@app.route('homepage/')
def homepage():
    return render_template('homepage.html')
