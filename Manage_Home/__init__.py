from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from os import path
from flask_login import LoginManager
from flask_session import Session
from datetime import timedelta


db = SQLAlchemy()


def create_App():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "1234567890"
    app.config['SQLALCHEMY_DATABASE_URI'] =os.getenv("database_url")
    app.config["UPLOAD_FOLDER"]='uploads/'
    app.config["MAX_CONTENT_LENGTH"]=16*1024*1024
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .views import view
    from .auth import auth
    from .models import User_Auth , Home_Data


    app.register_blueprint(view,url_prefix="/")
    app.register_blueprint(auth,url_prefix='/')

    create_database(app)

    login_manager=LoginManager()
    login_manager.login_view="auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(first_name):
        user= User_Auth.query.get(first_name)
        return user

    return app

def create_database(app):
    with app.app_context():
        db.create_all()





