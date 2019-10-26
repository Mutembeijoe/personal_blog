from flask import Blueprint, render_template
from app.users.forms import RegistrationForm

users = Blueprint('users', __name__)


@users.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', form = form )