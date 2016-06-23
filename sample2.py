#!/usr/bin/env python

import requests, json

requests.packages.urllib3.disable_warnings()

url = 'https://apic:8888/api/aaaLogin.json'


# these are Python dictionary objects:
payload = {
    "aaaUser": {
        "attributes": {
            "pwd": "1vtG@lw@y",
            "name": "admin"
        }
    }
}
headers = { 'content-type': "application/json" }

""" note the different quotes
>>> print(payload)
{'aaaUser': {'attributes': {'pwd': '1vtG@lw@y', 'name': 'admin'}}}
>>> json.dumps(payload)
'{"aaaUser": {"attributes": {"pwd": "1vtG@lw@y", "name": "admin"}}}'
"""

response = requests.post(url, data=json.dumps(payload), headers=headers)
token = response.cookies.get('APIC-cookie')

url = 'https://apic:8888/api/node/class/dhcpClient.json'
response = requests.get(url, cookies={'APIC-cookie': token})
print(response.text)


