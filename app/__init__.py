from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'



def create_app():
    app = Flask(__name__)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app.main.routes import main
    app.register_blueprint(main)


    return app
