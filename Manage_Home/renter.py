from flask import  Blueprint , render_template , request ,flash , current_app
from . import db 
from flask_login import  login_required  , current_user
from .models import Home_Data
import os
from .landlord import posted_houses
rent=Blueprint("rent", __name__)

@rent.route('/renter')
def renter():
    home = Home_Data.query.all()
    for house in home:
        print(house.photo_meta)
    return render_template("renter.html",home=home)