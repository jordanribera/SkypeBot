import requests
import json

url = 'http://spiralpower.net/files/skypebot/'
payload = {'message': 'Hello', 'sender_handle': 'foobar', 'sender_fullname': 'Foo McBar'}

r = requests.post(url, data=payload)

print(r.text)
