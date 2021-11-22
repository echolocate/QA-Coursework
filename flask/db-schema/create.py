from app import db, Users, Dogs

db.drop_all()
db.create_all()

testuser = Users(
    first_name='Grooty',
    last_name='Toot'
) # Extra: this section populates the table with an example entry
db.session.add(testuser)
db.session.commit()

testdogs = Dogs(
    dog_name = "Digby",
    breed = "Cujo",
    weight = 600 
)
db.session.add(testdogs)
db.session.commit()


print(f"Users first name is: {testuser.first_name}")
print(f"Dog name is: {testdogs.dog_name}")
print(f"Dog breed is: {testdogs.breed}")
print(f"Dog weight is: {testdogs.weight}")