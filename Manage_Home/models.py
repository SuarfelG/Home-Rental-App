from . import db
from flask_login import UserMixin

class User_Auth (db.Model , UserMixin):
    __tablename__="User_Auth"

    id=db.Column(db.Integer , primary_key=True)
    first_name=db.Column(db.String(50), nullable=False , unique=True)
    middle_name=db.Column(db.String(50), nullable=False)
    last_name=db.Column(db.String(50), nullable=False)
    email=db.Column(db.String(50), nullable=False)
    password=db.Column(db.String(255), nullable=False)
    AccountType=db.Column(db.String(10),nullable=False)
    user_id=db.relationship("Home_Data")


class Home_Data (db.Model, UserMixin ):
    __tablename__="Home_Data"

    
    Home_id=db.Column(db.Integer , primary_key=True)
    location=db.Column(db.String(50), nullable=False)
    rooms=db.Column(db.String(30), nullable=False)
    Home_Description=db.Column(db.String(200), nullable=False)
    photo_meta=db.Column(db.String(200), nullable=False)
    video_meta=db.Column(db.String(200), nullable=False)
    photo_address=db.Column(db.String(200), nullable=False)
    video_address=db.Column(db.String(200), nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey(User_Auth.id) ,nullable=False)
    price=db.Column(db.Integer)
    owner_address=db.Column(db.String(200), nullable=False)