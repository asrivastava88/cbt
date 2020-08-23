import requests
import json
from pprint import pprint

# Set up connection parameters in a dictionary
# Router IP is from Reserved Sandbox Lab of Cisco CSR-1000v
rtr = {"ip": "10.10.20.48", "port": "443",
       "user": "developer", "pass": "C1sco12345"}

# Set REST API Headers
headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json'}

url = f"https://{rtr['ip']}:{rtr['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"
print(url)

pull_response = requests.get(url, headers=headers, auth=(
    rtr['user'], rtr['pass']), verify=False)

api_data = pull_response.json()
print("\n")
print('*' * 50)
pprint(api_data["Cisco-IOS-XE-interfaces-oper:interface"]["description"])
print('*' * 50)

if api_data["Cisco-IOS-XE-interfaces-oper:interface"]["admin-status"] == 'if-state-up':
    print("\nInterface is up!")
