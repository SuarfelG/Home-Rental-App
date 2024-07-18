from flask import  Blueprint , render_template , request ,flash , current_app
from . import db 
from flask_login import login_manager , login_required ,login_user , current_user
from .models import User_Auth , Home_Data
from werkzeug.security import generate_password_hash , check_password_hash
from werkzeug.utils import secure_filename
import os
auth=Blueprint("auth", __name__)



@auth.route("/landlord", methods=["POST", "GET"])
@login_required
def landlord():
        if current_user.AccountType=='Renter':
                flash("Can Not Access This Page", category="error")
                return render_template ("home.html")               
        if request.method=="POST":
                location=request.form.get("location")
                room=request.form.get("rooms")
                Description=request.form.get("Description")
                photo = request.files['photo']
                video = request.files['video']

                photo_path = os.path.join(current_app.config['UPLOAD_FOLDER'], photo.filename)
                video_path = os.path.join(current_app.config['UPLOAD_FOLDER'], video.filename)
                if (photo and photo.filename) and  (video and video.filename):
                       photo.save(photo_path)
                       video.save(video_path)

                newupload=Home_Data(location=location , rooms=room , Home_Description=Description , photo_meta=photo_path , video_meta=video_path , user_id=current_user.id)
                db.session.add(newupload)
                db.session.commit()
                flash("Uploaded Succesfuly" , category="success")
                return render_template("home.html")

        return render_template("landlord.html")

@auth.route("/modify" , methods=["POST","GET"])
@login_required
def modify():
         if current_user.AccountType=='Renter':
                flash("Can Not Access This Page", category="error")
                return render_template ("home.html")   
         home=Home_Data.query.filter_by(user_id=current_user.id)
   
         return render_template("modify.html", home=home)

@auth.route("/modifyhome/<value>" , methods=["POST","GET"])
def modifyhome(value):
         home=Home_Data.query.filter_by(Home_id=value).first()
         if request.method=="POST":
                location=request.form.get("location")
                room=request.form.get("rooms")
                Description=request.form.get("Description")
                photo = request.files['photo']
                video = request.files['video']

                photo_path = os.path.join(current_app.config['UPLOAD_FOLDER'], photo.filename)
                video_path = os.path.join(current_app.config['UPLOAD_FOLDER'], video.filename)

                if (photo and photo.filename) and  (video and video.filename):
                       photo.save(photo_path)
                       video.save(video_path)
                       home.photo_meta=photo_path
                       home.video_meta=video_path
                home.location=location
                home.rooms=room
                home.Home_Description=Description
                home.user_id=current_user.id
                db.session.commit()

         return render_template("modify.html", mod=home)


@auth.route("/login", methods=["POST","GET"])
def login():
        if request.method=="POST":
             password=request.form.get('password')
             email=request.form.get('email')
             EmailExist=User_Auth.query.filter_by(email=email).first()

             if EmailExist:
                    if check_password_hash(EmailExist.password,password):
                            flash("Logged In Successfuly", category="success")
                            login_user(EmailExist)
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
                login_user(newUser_Auth)
                flash("Signed in Successfuly" , category="success")
                return render_template("landlord.html")

                
        
    return render_template("signup.html")

