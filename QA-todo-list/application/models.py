from application import db

class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(30), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)