# Import everything we need
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import os

app = Flask(__name__) # Declare Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI") # Set the connection string to connect to a database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # Declare SQLAlchemy object

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(70), nullable=False)
    # agent_email = db.Column(db.String(50), nullable=False)
    # agent_phone = db.Column(db.Integer(20))
    band = db.relationship('Band', backref='agent')

class Band(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    # email = db.Column(db.String(50), nullable=False)
    # phone = db.Column(db.Integer(20))
    # genre = db.Column(db.String(20))
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'), nullable=False)

if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')

