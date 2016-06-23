import requests
response = requests.get('http://cisco.com/')
print(response.text)
print(response.ok)
print(response.status_code)

###

import requests
url = 'https://api.stackexchange.com/2.2/search?intitle=python&site=stackoverflow'
response = requests.get(url)
if response.ok:
    print(response.text)
else:
    print(response.status_code)

###

import requests, json
url = 'https://api.stackexchange.com/2.2/search?intitle=python&site=stackoverflow'
response = requests.get(url)
if response.ok:
    print(json.dumps(response.json(), indent=2))
else:
    print(response.status_code)

###

import requests, json
url = 'https://msesandbox.cisco.com/api/contextaware/v1/maps'
response = requests.get(url)
if response.ok:
    print(json.dumps(response.json(), indent=2))
else:
    print(response.status_code)

###

import requests
url = 'https://msesandbox.cisco.com/api/contextaware/v1/maps'
headers = {"authorization": "Basic bGVhcm5pbmc6bGVhcm5pbmc=="}
response = requests.get(url, headers=headers)
if response.ok:
    print(json.dumps(response.json(), indent=2))
else:
    print(response.status_code)

###

import requests
url = 'https://msesandbox.cisco.com/api/contextaware/v1/maps'
headers = {"authorization": "Basic bGVhcm5pbmc6bGVhcm5pbmc==",
    "accept": "application/json"}
response = requests.get(url, headers=headers)
if response.ok:
    print(json.dumps(response.json(), indent=2))
else:
    print(response.status_code)


###

import requests
url = 'https://msesandbox.cisco.com/api/contextaware/v1/maps'
auth = requests.auth.HTTPBasicAuth("learning", "learning")
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers, auth=auth)
if response.ok:
    print(json.dumps(response.json(), indent=2))
else:
    print(response.status_code)

