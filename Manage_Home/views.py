from flask import Blueprint , render_template
from . import db

view=Blueprint("views" , __name__)

@view.route("/")
def Home ():
    return render_template("home.html")