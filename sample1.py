#!/usr/bin/env python

import requests, json
requests.packages.urllib3.disable_warnings()

url = "https://apic:8888/api/aaaLogin.json"

payload = {
    "aaaUser": {
        "attributes": {
            "pwd": "1vtG@lw@y",
            "name": "admin"
        }
    }
}

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    }

response = requests.request("POST", url, data=json.dumps(payload), headers=headers, verify=True)

print(response.text)
