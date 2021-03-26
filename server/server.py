import os
from flask import Flask
from flask import request, make_response, jsonify
from flask_cors import CORS
from database.service import *

app = Flask(__name__, static_folder="./builder/static", template_folder="./build")
CORS(app) #Cross Origin Resource Sharing

@app.route("/", methods=['GET'])
def index():
    return "Updating"

@app.route("/update", methods=['GET', 'POST'])
def update_data():
    data = request.get_json()
  
    # Get email (key) from request
    email = data['email']
    email = "'" + email + "'"

    # Get an update value for status
    new_status = data['new_status']
    new_status = "'" + new_status + "'"

    update_data_with_key('database/users.db','USERS', 'user_email',email,
                                'user_status',new_status)
    response = {'result': "Updated"}
    return make_response(jsonify(response))

if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=5000)

