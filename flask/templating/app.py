from flask import Flask, render_template

app = Flask(__name__)

@app.route('/exercise')
def names_with_b():
    names = ["ben", "harry", "bob", "jay", "matt", "bill"]
    return render_template('exercise.html',names=names)

@app.route('/ben')
def ben():
    return render_template('ben.html')

@app.route('/harry')
def harry():
    return render_template('harry.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')