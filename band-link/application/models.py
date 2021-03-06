from application import db

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