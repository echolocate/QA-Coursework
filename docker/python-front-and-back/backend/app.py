from flask import Flask
from os import getenv
from random import randint

app = Flask(__name__)

@app.route("/hostname")
def hostname():
    return str(getenv("HOSTNAME"))

@app.route("/random")
def random_generator():
    return str(randint(0, 9999))

if __name__=="__main__":
    app.run(host = "0.0.0.0", port = 5001, debug = True)
