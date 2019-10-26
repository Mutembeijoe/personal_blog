from flask import Blueprint, render_template, flash, redirect, url_for,request
from app.users.forms import RegistrationForm
from app import bcrypt,db
from app.models import User
from flask_login import login_user,current_user


users = Blueprint('users', __name__)

@users.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account was successfully created, you can now login!', "success")
        return redirect(url_for('main.home'))
    return render_template('register.html', form = form )

@users.route("/login", methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Invalid email or password', 'danger')
    return render_template('login.html', form = form)