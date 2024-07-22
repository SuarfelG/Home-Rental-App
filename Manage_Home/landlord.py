from flask import  Blueprint , render_template , request ,flash , current_app
from . import db 
from flask_login import  login_required  , current_user
from .models import Home_Data
import os
land=Blueprint("landlord", __name__)


@land.route("/landlord", methods=["POST", "GET"])
@login_required
def landlord():
        if current_user.AccountType=='Renter':
                flash("Can Not Access This Page", category="error")
                return render_template ("home.html")       
        return render_template ("landlord.html")        
@land.route('/posted_houses')
@login_required
def posted_houses():
        if current_user.AccountType=='Renter':
                flash("Can Not Access This Page", category="error")
                return render_template ("home.html")    
        home=Home_Data.query.filter_by(user_id=current_user.id)
        return render_template ("posted_houses.html" , home=home)

@land.route("/Post_House", methods=["POST", "GET"])
@login_required
def Post_House():
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
                photo_pass=photo.filename
                if (photo and photo.filename) and  (video and video.filename):
                       photo.save(photo_path)
                       video.save(video_path)

                newupload=Home_Data(location=location , rooms=room , Home_Description=Description , photo_meta=photo_path , video_meta=video_path , user_id=current_user.id)
                db.session.add(newupload)
                db.session.commit()
                flash("Uploaded Succesfuly" , category="success")
                return render_template("home.html")

        return render_template("Post_house.html")



@land.route("/update" , methods=["POST","GET"])
@login_required
def modify():
         if current_user.AccountType=='Renter':
                flash("Can Not Access This Page", category="error")
                return render_template ("home.html")    
         if current_user.AccountType=='Renter':
                flash("Can Not Access This Page", category="error")
                return render_template ("home.html")   
         home=Home_Data.query.filter_by(user_id=current_user.id)
   
         return render_template("Update_Post.html", home=home)

@land.route("/updatehome/<value>" , methods=["POST","GET"])
@login_required
def updatehome(value):
         if current_user.AccountType=='Renter':
                flash("Can Not Access This Page", category="error")
                return render_template ("home.html")    
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

         return render_template("Update_Post.html", mod=home)
@land.route("/delete" , methods=["POST","GET"])
@login_required
def delete():
       if current_user.AccountType=='Renter':
                flash("Can Not Access This Page", category="error")
                return render_template ("home.html")    
       if current_user.AccountType=='Renter':
                flash("Can Not Access This Page", category="error")
                return render_template ("home.html")   
       home=Home_Data.query.filter_by(user_id=current_user.id)
       return render_template ("delete.html", home=home)
@land.route("deletehome/<value>",methods=["POST","GET"])
@login_required
def deletehome(value):
       if current_user.AccountType=='Renter':
                flash("Can Not Access This Page", category="error")
                return render_template ("home.html")    
       try:
                home=Home_Data.query.filter_by(Home_id=value).first()
                db.session.delete(home)
                db.session.commit()
                flash("Post Successfuly Deleted" , category="success")
                return render_template ("home.html")
       except:
                flash("Unable To Delete The Post Try Again", category="error")
                return render_template ("home.html")