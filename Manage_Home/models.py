from . import db

class User (db.Model):
    __tablename__="User Authentication"

    id=db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(50), nullable=False)
    middle_name=db.Column(db.String(50), nullable=False)
    last_name=db.Column(db.String(50), nullable=False)
    email=db.Column(db.String(50), nullable=False)
    password=db.Column(db.String(50), nullable=False)
    AccountType=db.Column(db.Boolean,nullable=False)