from flask import Flask, Response, request, jsonify
app = Flask(__name__)

information = {'name':'Someguy Somewhere','age':'32', 'occupation':'Somejob'}

@app.route('/')
@app.route('/info', methods=['GET'])
def get_text():
    # The API request will return text containing the information as a JSON object.
    return jsonify(information)

# Here we will add functionality to add the information dictionary. The new key is defined in the URL, and the value of the key is in the sent data. We also want to add a check for pre-existence, so that we do not update existing entires (we want to save that for PUT requests).
@app.route('/info/add/<string:key>', methods=['POST'])
def post_text(key):
    # adding the new key-value pair
    if key not in information:
        information[key] = request.data.decode('utf-8')
        return Response(key + " added to information with value: " + request.data.decode('utf-8'), mimetype='text/plain')
    else:
        return Response(key + " already exists.", mimetype='text/plain')

# We will implement update functionality (PUT request) with the same URL as the route for POST requests, but with a PUT method. Similar to before, we want to check the dictionary for pre-existence so that we only implement changes if the key already exists.
@app.route('/info/update/<string:key>', methods=['PUT'])
def put_text(key):
    if key in information:
        information[key] = request.data.decode('utf-8')
        return Response(key + " changed to: " + request.data.decode('utf-8'), mimetype='text/plain')
    else:
        return Response(key + " not found.", mimetype='text/plain')

# Finally, we add a function so that if the request is DELETE, we delete that key from the dictionary.
@app.route('/info/delete', methods=['DELETE'])
def delete_text():
    key = request.data.decode('utf-8')
    if key in information:
        information.pop(key)
        return Response(key + " deleted from information. ", mimetype='text/plain')
    else:
        return Response(key + " not found.", mimetype='text/plain')

# Make app callabale from the command line
if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')