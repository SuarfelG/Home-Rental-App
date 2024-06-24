from flask import  Blueprint , render_template , request ,flash 

auth=Blueprint("auth", __name__)



@auth.route("/login", methods=["POST","GET"])
def login():
        if request.method=="POST":
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
        
        if (len(Name)<4):
                flash("Name is too short" , category="error")
        elif (len(Father_Name)<4):
                flash("Father_Name is too short" , category="error")
        elif(len(Email)<4):
                flash("Email is too short" , category="error")
        elif(len(Password)<4):
                flash("Password is too short" , category="error")
        else:
                flash("Signed in Successfuly" , category="success")
                return 'home.html'
        
    return render_template("signup.html")