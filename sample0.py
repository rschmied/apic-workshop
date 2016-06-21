import requests

url = "https://apic:8888/api/aaaLogin.json"

payload = '{ "aaaUser": {"attributes": {"pwd": "1vtG@lw@y", "name": "admin" }}}'
headers = { 'content-type': "application/json" }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
