# Sample Code for APIC DC Workshop
This project contains a few code samples / script to illustrate the use of APIC DC APIs. These examples are extremely simple:

- *login to the controller* using a username and a password. The result is an access token (in a cookie) to authorize subsequent requests
- *retrieve a list of managed objects* (here: DHCP client IP address of devices / objects known to the fabric)

This is done via a few different approaches

- `curl.sh`, illustrating the use of Curl and JQ
- `APIC.postman_collection`, contains two Postman requests
- `sample0.py`, login to the controller using Requests library, auth data as JSON string
- `sample1.py`, as `sample0.py`, auth data as Python Object converted to JSON on the fly
- `sample2.py`, login to the controller, retrieving DHCP objects using the provided APIC Cobra library

### Links
- APIC Cisco APIC Python SDK Documentation: <https://apic:8888/cobra/index.html>
- APIC Management Information Model Reference: <https://apic:8888/doc/html/>
- APIC Cobra SDK Download: <https://apic:8888/cobra/_downloads/>
- ACI Dev Community <https://acidev.cisco.com>

### Tools
*Tunneling tools* allows you to easily share a web service on your local development machine without messing with DNS and firewall settings. They can also be used to talk to use the tool as a 'MITM' which relays (and inspects) the traffic to the destination (a controller, for example)

- <http://localtunnel.me/>
- <https://ngrok.com/>

*Others*

- curl <https://curl.haxx.se/>
- jq is a lightweight and flexible command-line JSON processor <https://stedolan.github.io/jq/>


### Common Issues
#### Virtualenv
If you want to use this with virtualenv, make sure to clone the repo first **then** create the Python virtual environment:

	$ git clone https://github.com/rschmied/apic-workshop.git
	$ virtualenv apic-workshop
	$ cd apic-workshop
	$ source bin/activate


#### Connection Reset
If you do see a connection reset like this when working with requests and Python 2.7

	requests.exceptions.ConnectionError: ('Connection aborted.', error(54, 'Connection reset by peer'))

then this indicates an issue with TLS and the OpenSSL implementation on your machine. This

	$ pip install --use-wheel pyopenssl ndg-httpsclient

usually solves the problem.


#### Certificate Verification 1
Certification verification will fail for self signed certificates. Python requests does not use the system certificate stores (at least not on Windows and the Mac). There are basically two options to work around this:

1) use `verify=False` with your requests, like shown here:

	response = requests.request("POST", url, data=payload, headers=headers, verify=False)

2) install the self signed certificate into the requests root certificate store. This is located in `[...]/lib/python-2.7/site-packages/requests/cacert.pem`. Just add the included (PEM encoded) `apic.cer` certificate to the top of that file and save it. The actual location of the `cacert.pem` file depends whether you use a virtual environment or not.


#### Certificate Verification 2
If you see a warning like this

	[...] SubjectAltNameWarning: Certificate for apic has no `subjectAltName`, falling back to check for a `commonName` for now. [...]

then this also indicates an issue of the used certificate. This warning can be suppressed by calling the following function within your script after importing the requests library:

	requests.packages.urllib3.disable_warnings()


#### Warning
Of course, these 'workarounds' **should only be applied** in a test-environment where self-signed certificates are more likely to be seen. Don't ever do these things in a production environment. Properly issued certificates with the right attributes and a matching FQDN / DNS entry, Common Name, Subject Alternative name and key usage are **important**!


### Disclaimer
The examples and code in the presentation and this repository are for **Learning and Educational purposes**. The samples were created with the **goals of clarity and ease of understanding**. If you are writing code for a real application, you would write the code in a more efficient and structured style.

