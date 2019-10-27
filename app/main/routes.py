from flask import Blueprint, render_template

from app.models import Post

main = Blueprint('main',__name__)

@main.route('/')
@main.route('/home')
@main.route('/home/<string:category>')
def home(category = None):
    if category:
        posts = Post.query.filter_by(category=category)
    else:
        posts = Post.query.all()
    return render_template('home.html', posts=posts, title = 'Home')