from app import db, Countries, Cities

db.drop_all()
db.create_all() # Creates all table classes defined

uk = Countries(name = 'United Kingdom') #Add example to countries table
db.session.add(uk)
db.session.commit()

# Here we reference the country that london belongs to using 'country', this is what we named the backref variable in db.relationship()
ldn = Cities(name='London', country = uk)
mcr = Cities(name='Manchester', country = Countries.query.filter_by(name='United Kingdom').first())

db.session.add(ldn)
db.session.add(mcr)
db.session.commit()

print(f"Cities in the UK are: {uk.cities[0].name}, {uk.cities[1].name}")
print(f"London's country is: {ldn.country.name}")
print(f"Manchester's country is: {mcr.country.name}")

for city in uk.cities:
    print(city.name)