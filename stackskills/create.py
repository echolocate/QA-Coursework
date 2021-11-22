from app import db, Users

db.drop_all()
db.create_all()

testuser = Users(
    firstname='Nancy',
    lastname='Spungeon',
    email="NancyVicious@groupie.com",
    pwdhash="sexndrugs") 
    
db.session.add(testuser)
db.session.commit()