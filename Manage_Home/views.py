from flask import Blueprint , render_template
from . import db

view=Blueprint("views" , __name__)

@view.route("/")
def Home ():
    return render_template("home.html")
@view.route("/signup")
def signup ():
    return render_template("signup.html")
@view.route("/login")
def login ():
    return render_template("login.html")
@view.route("/about")
def about():
    return render_template("about.html")