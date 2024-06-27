from . import db

class User_Auth (db.Model):
    __tablename__="User_Auth"

    id=db.Column(db.Integer , primary_key=True)
    first_name=db.Column(db.String(50), nullable=False , unique=True)
    middle_name=db.Column(db.String(50), nullable=False)
    last_name=db.Column(db.String(50), nullable=False)
    email=db.Column(db.String(50), nullable=False)
    password=db.Column(db.String(255), nullable=False)
    AccountType=db.Column(db.String(10),nullable=False)