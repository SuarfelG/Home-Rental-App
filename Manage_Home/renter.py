from flask import  Blueprint , render_template , request ,flash , current_app , redirect
from . import db 
from flask_login import  login_required  , current_user
from .models import Home_Data
import os
from .landlord import posted_houses
rent=Blueprint("rent", __name__)

@rent.route('/renter')
@login_required
def renter():
    if current_user.AccountType.lower()!="renter":
        return redirect ("landlord")
    home = Home_Data.query.all()
    return render_template("renter.html",home=home)