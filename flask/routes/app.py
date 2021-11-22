from flask import redirect, url_for
from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Home Page'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/squared/<int:number>,<int:number_two>')
def squared(number,number_two):
    return str(number**number_two)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)