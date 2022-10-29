from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_user, logout_user, current_user
from .forms import LoginForm, UserForm, ModifyForm
from app.models import Customer
from werkzeug.security import check_password_hash
from email_validator import validate_email

auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/login', methods=["GET", "POST"])
def loginPage():
    form = LoginForm()
    if request.method == "POST":
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = Customer.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    login_user(user)
                    return redirect(url_for('index'))
                else:
                    flash('That is not your password!!!', 'warning')
            else:
                flash('This user does not exist. Please try again...', 'warning')
    return render_template('login.html', form=form)

@auth.route('/signup', methods=["GET", "POST"])
def signupPage():
    form = UserForm()
    if request.method == "POST":
        if form.validate():
            firstname = (form.firstname.data).lower()
            lastname = (form.lastname.data).lower()
            username = (form.username.data).lower()
            email = form.email.data
            password = form.password.data
            uq_un = Customer.query.filter_by(username=username).first()
            uq_em = Customer.query.filter_by(email=email).first()
            if uq_un and uq_em:
                flash('That username AND email belong to an account.', 'warning')
            elif uq_un:
                flash('That username already belongs to an account.', 'warning')
            elif uq_em:
                flash('That email already belongs to an account.', 'warning')
            else:
                user = Customer(firstname, lastname, username, email, password)
                try:
                    email = validate_email(email)
                except:
                    flash('That is not a valid email address.', 'warning')
                    return render_template('signup.html', form=form)
                user.saveToDB()
                flash('User Created Successfully!', 'success')
                return redirect(url_for('auth.loginPage'))
    return render_template('signup.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    flash('Logout Successful.')
    return redirect(url_for('auth.loginPage'))

@auth.route('/profile/<username>')
def viewProfile(username):
    profile = Customer.query.filter_by(username=current_user.username).first()
    if username != current_user.username:
        return redirect(url_for('auth.logout'))
    else:
        return render_template('profile.html', profile=profile)

@auth.route('/modify_profile/<username>', methods=["GET", "POST"])
def modifyProfile(username):
    profile = Customer.query.filter_by(username=current_user.username).first()
    form = ModifyForm()
    if request.method == "POST":
        if form.validate():
            firstname = form.firstname.data
            lastname = form.lastname.data
            username = form.username.data
            email = form.email.data
            password = form.password.data
            try:
                validate_email(email)
            except:
                email_error = "That is not a valid email address."
                return render_template('profile.html', form=form, email_error=email_error, profile=profile)
            if password == '':
                profile.modify(firstname, lastname, username, email)
            else:
                profile.modify(firstname, lastname, username, email, password)
            return redirect(url_for('auth.viewProfile', profile=profile, username=current_user.username))
    return render_template('modify_profile.html', form=form, profile=profile)