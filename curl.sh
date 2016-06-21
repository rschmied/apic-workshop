#!/bin/bash

# this example uses jq to digest the returned JSON
# https://stedolan.github.io/jq/download/

# the example at the bottom uses XML data instead of JSON to login

#set -x 

a='{
  "aaaUser": {
    "attributes": {
      "pwd": "1vtG@lw@y",
      "name": "admin"
    }
  }
}'

aaaData=$(echo $a | curl -sv -X POST https://apic:8888/api/aaaLogin.json -d @- \
		  | jq '.imdata[0]["aaaLogin"]["attributes"]')

echo "$aaaData"
read

cookie="APIC-Cookie="$(echo $aaaData | jq -r '.["token"]')
node=$(echo $aaaData | jq -r '.["node"]')

curl -sv -b "$cookie" https://apic:8888/api/node/class/$node/dhcpClient.json | jq '.'

exit


# XML
a='<aaaUser pwd="1vtG@lw@y" name="admin"></aaaUser>'
echo $a | curl -sv -X POST https://apic:8888/api/aaaLogin.xml -d @-


