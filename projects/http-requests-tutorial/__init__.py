import requests
api = 'http://localhost:5000'

print('HTTP GET Request (text):')
response = requests.get(api + '/get/text')
print('Response: ', response.text)

print('HTTP POST Request (text):')
response = requests.post(api + '/post/text', 'My Data')
print('Response: ', response.text)

print('HTTP GET Request (json):')
response = requests.get(api + '/get/json')
print('Whole Response: ' + str(response.json()))
print('"data" Property of the Response: ' +  str(response.json()["data"]))

print('HTTP POST Request (json):')
response = requests.post(api + '/post/json', json={"message": "mydata"})
print('Whole Response: ' + str(response.json()))
print('"data" Property of the Response: ' +  str(response.json()["data"]))