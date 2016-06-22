#!/usr/bin/env python

import logging, json

from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession


# uncomment the below to get more verbose output
# for debugging
"""
import httplib as http_client
http_client.HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
"""

session = LoginSession('https://apic:8888', 'admin', '1vtG@lw@y')
moDir = MoDirectory(session)
moDir.login()
tenant1Mo = moDir.lookupByClass("dhcpClient")

for c in tenant1Mo:
	print(c.dn, c.model, c.name, c.ip)

moDir.logout()


