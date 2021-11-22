from flask import Flask
import requests
from os import getenv

app = Flask(__name__)

@app.route("/")
def home():
    hostname = getenv("HOSTNAME")
    backend_hostname = requests.get("http://backend:5001/hostname")
    random = requests.get("http://backend:5001/random")
    colour = "blue"
    return f"<body style='background-color:{colour};'>\n<h1>Hello friend.</h1>\n\n<h2>I'm currently running in {hostname}.</h2>\n\n<h2>The backend I'm chatting with is running in {backend_hostname.text}</h2>\n\n<h3>The backend gave me this to show you: {random.text}</h3>"

if __name__=="__main__":
	app.run(host = "0.0.0.0", port = 5000, debug = True)
