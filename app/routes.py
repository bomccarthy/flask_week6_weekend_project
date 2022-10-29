from flask import render_template, request, redirect, url_for
from app import app

from app.models import Customer
import app.prodFunc

@app.route('/')
def index():
    return render_template('index.html')
