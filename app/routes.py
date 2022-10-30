from flask import render_template, request, redirect, url_for
from app import apps

from app.models import Customer
import app.prodFunc

@apps.route('/')
def homepage():
    return render_template('index.html')
