from application import app
import requests

@app.route('/get/sport', methods=['GET']) 
def sport():
    number = requests.get('http://api:5000/get/number').text
    letter = requests.get('http://api:5000/get/letter').text
    if number == "1" and letter == "a":
        return "Football"
    elif number == "1" and letter == "b":
        return "Badminton"
    elif number == "1" and letter == "c":
        return "Hockey"
    else:
        return "Boxing"