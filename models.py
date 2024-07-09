from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    user_id = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    phone = db.Column(db.String)

class Organisation(db.Model):
    org_id = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    users = db.relationship('User', secondary='user_organisations', backref='organisations')

class UserOrganisations(db.Model):
    __tablename__ = 'user_organisations'
    user_id = db.Column(db.String, db.ForeignKey('user.user_id'), primary_key=True)
    org_id = db.Column(db.String, db.ForeignKey('organisation.org_id'), primary_key=True)
