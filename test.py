import os

import requests

webhook = 'https://chat.googleapis.com/v1/spaces/AAAACmWw6q8/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=ly36Lxs0rOMA2c6nJzeIwE1lfU3gQjCQ3A6sCgRSRB4%3D'

WEBHOOK_URL = os.environ[webhook]

title = 'Hi'
subtitle = 'Hello'
paragraph = 'bye.'
widget = {'textParagraph': {'text': paragraph}}
res = requests.post(
    WEBHOOK_URL,
    json={
        'cards': [
            {
                'header': {
                    'title': title,
                    'subtitle': subtitle,
                },
                'sections': [{'widgets': [widget]}],
            }
        ]
    },
)
print(res.json())