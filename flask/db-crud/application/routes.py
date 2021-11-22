from application import app, db
from application.models import Games

@app.route('/add')
def add():
    new_game = Games(name="New Game")
    db.session.add(new_game)
    db.session.commit()
    return "Added new game to database"

@app.route('/read')
def read():
    all_games = Games.query.all() # SELECT * FROM games;
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string

@app.route('/update/<name>')
def update(name):
    first_game = Games.query.first() # SELECT * FROM games LIMIT 1;
    first_game.name = name
    db.session.commit()
    return first_game.name

@app.route('/delete')
def delete():
    delete_game = Games.query.first()
    db.session.delete(delete_game)
    db.session.commit()
    return delete_game.name
