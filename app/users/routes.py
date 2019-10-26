from flask import Blueprint, render_template


users = Blueprint('users', __name__)


@users.route('/register', methods = ['GET', 'POST'])
def register():
    return render_template('register.html')