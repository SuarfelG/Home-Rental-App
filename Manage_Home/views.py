from flask import Blueprint , render_template
from . import db
from flask_login import login_required
view=Blueprint("views" , __name__)

@view.route("/")
def Home ():
    return render_template("home.html")
@view.route("/about")
def about():
    return render_template ("about.html")