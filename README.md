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

### Disclaimer

The examples and code in the presentation and this repository are for **Learning and Educational purposes**.The samples were created with the **goals of clarity and ease of understanding**.If you are writing code for a real application, you would write the code in a more efficient and structured style.