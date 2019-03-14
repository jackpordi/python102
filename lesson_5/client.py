import requests
import json

myname = input("Please enter your name: ")


def get_messages():
    return json.loads(
        requests.get('http://localhost:5000/get_messages').text)


def send_message(message):
    data = {
        'name': myname,
        'message': message
    }

    return requests.post('http://localhost:5000/submit_messages', json=data)


while True:
    for datetime, handle, msg in get_messages():
        print(handle, ":", msg)
    message = input("Enter a message: ")
    send_message(message)
