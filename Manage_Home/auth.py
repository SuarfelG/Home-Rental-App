from flask import  Blueprint , render_template , request ,flash 
from flask_wtf import FlaskForm
from wtforms import StringField ,RadioField , SubmitField
from wtforms.validators import DataRequired
from . import db
from .models import User
auth=Blueprint("auth", __name__)




class RegstrationForm (FlaskForm):
       first_name=StringField('first_name' , validators=[DataRequired()])
       middle_name=StringField('first_name' , validators=[DataRequired()])
       last_name=StringField('first_name' , validators=[DataRequired()])
       pasword=StringField('first_name' , validators=[DataRequired()])
       AccountType=RadioField ("AccountType", choices=(["landlord",True] ,["renter",False] ))
       Submit=SubmitField('signup')


@auth.route("/login", methods=["POST","GET"])
def login():
        if request.method=="POST":
             id = request.form.get('id')
             first_name=request.form.get('first_name')
             middle_name=request.form.get('middle_name')
             last_name=request.form.get('last_name')
             password=request.form.get('password')
             email=request.form.get('email')
             AccountType=request.form.get('AccountType')

             EmailExist=User.query.filter_by(email).first()
             


             flash("Logged In Successfuly", category="success")
             return render_template("signup.html")
                      
        return render_template("login.html")

@auth.route("/signup", methods=["POST","GET"])
def signup():
    if request.method=="POST":
        Name=request.form.get("Name")
        Father_Name=request.form.get("Middle")
        Email=request.form.get("Email")
        Password=request.form.get("Password")
        user_type=request.form.get("user_type")
        
        if (len(Name)<3):
                flash("Name is too short" , category="error")
        elif (len(Father_Name)<3):
                flash("Father_Name is too short" , category="error")
        elif(len(Email)<4):
                flash("Email is too short" , category="error")
        elif(len(Password))<4:
                flash("Password is too short" , category="error")
        else:
                flash("Signed in Successfuly" , category="success")
                return 'home.html'
        
    return render_template("signup.html")