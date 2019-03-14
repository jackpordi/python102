import json

from flask import Flask, jsonify, request, render_template
from datetime import datetime

messages = []
# Message format is timestamp, name, message

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    return render_template('./website/index.html')

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello!"


@app.route('/get_messages', methods=['GET'])
def get_messages():
    return jsonify(messages)


@app.route('/submit_messages', methods=['POST'])
def submit_messages():
    data = json.loads(request.data)
    name = data['name']
    message = data['message']
    messages.append((datetime.now(), name, message))

    for time, handle, msg in messages:
        print(time, handle, msg)

    return 'Submitted'


app.run(debug=True, port=80, host="0.0.0.0")
