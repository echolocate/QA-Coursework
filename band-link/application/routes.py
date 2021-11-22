from application import app, db
from application.models import Agent, Band

@app.route('/add/agent')
def add_agent():
    new_agent = Agent(name="New Agent")
    db.session.add(new_agent)
    db.session.commit()
    return "Added new agent to database"

@app.route('/add/band')
def add_band():
    new_band = Band(name="New Band")
    db.session.add(new_band)
    db.session.commit()
    return "Added new band to database"

@app.route('/read/agent')
def read_agent():
    all_agents = Agent.query.all()
    agent_string = ""
    for agent in all_agents:
        agent_string += "<br>"+ agent.name
    return agent_string

@app.route('/read/band')
def read_band():
    all_bands = Band.query.all()
    band_string = ""
    for band in all_bands:
        band_string += "<br>"+ band.name
    return band_string

# @app.route('/update/<name>')
# def update(name):
#     first_game = Games.query.first()
#     first_game.name = name
#     db.session.commit()
#     return first_game.name