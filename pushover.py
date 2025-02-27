# Send a pushover notification. Use PUSHOVER_USER and PUSHOVER_KEY environment variables.

import os
import requests

def send_pushover(title, message):
    user = os.environ.get('PUSHOVER_USER')
    key = os.environ.get('PUSHOVER_KEY')
    if not user or not key:
        print('PUSHOVER_USER and PUSHOVER_KEY environment variables not set.')
        return
    url = 'https://api.pushover.net/1/messages.json'
    data = {
        'token': key,
        'user': user,
        'title': title,
        'message': message,
    }
    requests.post(url, data=data)

if __name__ == '__main__':
    send_pushover('From your repo', 'Something happened!')