# Import everything we need
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import os

app = Flask(__name__) # Declare Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI") # Set the connection string to connect to a database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) # Declare SQLAlchemy object

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer(4), nullable=False)
    
class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.String(30), nullable=False)
    name = db.relationship('Products', backref='order')

class ProductOrder(db.Model):
    products_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
   
if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')