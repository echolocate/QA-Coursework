from flask import Flask # Import Flask class
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class
import os

app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI") # Set the connection string to connect to the database using an environment variable
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # Create SQLALchemy object

# Table schema
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    # dogs = db.relationship("Dogs", backref="owner")

# Exercise - create another table
class Dogs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dog_name = db.Column(db.String(30), nullable=False)
    breed = db.Column(db.String(30), nullable=False)
    weight = db.Column(db.Integer, nullable=False)
#   owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False))

if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')