from app import db, Agent, Band

db.drop_all()
db.create_all() # Creates all table classes defined

gb = Agent(name = 'Glitterbest') #Add example to agents table
db.session.add(gb)
db.session.commit()

# Here we reference the agent representing the band using 'agentbr', backref in db.relationship()
sp = Band(name='Sex Pistols',agent=gb)
wbl = Band(name='Wombles',agent=Agent.query.filter_by(name='Glitterbest').first())

db.session.add(sp)
db.session.add(wbl)
db.session.commit()

print(f"Bands represented by Glitterbest are: {gb.band[0].name}, {gb.band[1].name}")
print(f"Sex Pistols agent is: {sp.agent.name}")
print(f"WWombles agent is: {sp.agent.name}")