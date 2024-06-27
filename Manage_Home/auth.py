from flask import  Blueprint , render_template , request ,flash 
from flask_wtf import FlaskForm
from wtforms import StringField ,RadioField , SubmitField
from wtforms.validators import DataRequired
from . import db
from .models import User_Auth
from werkzeug.security import generate_password_hash , check_password_hash
auth=Blueprint("auth", __name__)


class RegstrationForm (FlaskForm):
       first_name=StringField('first_name' , validators=[DataRequired()])
       middle_name=StringField('first_name' , validators=[DataRequired()])
       last_name=StringField('first_name' , validators=[DataRequired()])
       pasword=StringField('first_name' , validators=[DataRequired()])
       AccountType=RadioField ("AccountType", choices=(["on",True] ,["off",False] ))
       Submit=SubmitField('signup')


@auth.route("/login", methods=["POST","GET"])
def login():
        if request.method=="POST":
             password=request.form.get('password')
             email=request.form.get('email')
             EmailExist=User_Auth.query.filter_by(email=email).first()

             if EmailExist:
                    if check_password_hash(EmailExist.password,password):
                            flash("Logged In Successfuly", category="success")
                            return render_template("home.html" )
                    else:
                           flash("Unkown User", category="error")
                           return render_template("signup.html")
             return render_template("signup.html")
                      
        return render_template("login.html")

@auth.route("/signup", methods=["POST","GET"])
def signup():
    if request.method=="POST":
        id = request.form.get('id')
        first_name=request.form.get('Name')
        middle_name=request.form.get('Middle')
        last_name=request.form.get('Last')
        email=request.form.get("Email")
        password=request.form.get("password")
        AccountType=request.form.get('flexRadioDefault')

        EmailExist=User_Auth.query.filter_by(email=email).first()

        
        if EmailExist:
                flash("Email Already Exist" , category="error")
        elif (len(first_name)<3):
                flash("Name is too short" , category="error")
        elif (len(middle_name)<3):
                flash("Middle Name is too short" , category="error")
        elif (len(last_name)<3):
                flash("Last Name is too short" , category="error")
        elif(len(email)<4):
                flash("Email is too short" , category="error")
        elif(len(password))<4:
                flash("Password is too short" , category="error")
        else:
                newUser_Auth=User_Auth(first_name=first_name , middle_name=middle_name , last_name=last_name ,email=email , password=generate_password_hash(password, method='pbkdf2:sha256')  , AccountType=AccountType )
                db.session.add(newUser_Auth)
                db.session.commit()
                flash("Signed in Successfuly" , category="success")
                return render_template("home.html")
        
    return render_template("signup.html")