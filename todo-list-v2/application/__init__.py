from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import uuid

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")
app.config['SECRET_KEY'] = str(uuid.uuid4())

db = SQLAlchemy(app)

# if getenv("CREATE_SCHEMA").lower() == "true":
#     db.drop_all()
#     db.create_all()

from application import routes