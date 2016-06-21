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


### Disclaimer

The examples and code in this presentation are for **Learning and Educational purposes**.The samples were created with the **goals of clarity and ease of understanding**.If you are writing code for a real application, you would write the code in a more efficient and structured style.