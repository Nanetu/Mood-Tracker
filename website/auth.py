from flask import Blueprint, render_template, redirect, request, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect Password!", category="error")
        else:
            flash("User doesnt exist!", category="error")
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email already exists!", category="error")
            return redirect(url_for('auth.login'))
        elif len(email) <4:
            flash("Email must be greater than 4 characters", category="error")
        elif len(firstName)< 2:
            flash("Firstname must be greater than 1 character", category="error")
        elif password1 != password2:
            flash("Passwords do no match", category="error")
        elif len(password1) <7:
            flash("Password must be atleast 7 characters", category="error")
        else:
            new_user = User(email=email, firstName=firstName, password=generate_password_hash(password1, method='scrypt'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Accont created", category="success")
            return redirect(url_for('views.home'))
    return render_template("signup.html", user=current_user)