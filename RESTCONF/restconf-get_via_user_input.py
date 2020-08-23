# To convert Username:password into Base64 encoded value for "Authorization" header.
import base64
# To do HTTP requests - like GET, POST, DELETE, etc.
import requests
# To convert JSON dictionary to Python objects and vice versa.
import json
# To print the dictionary/object data in structured way.
from pprint import pprint
import getpass                      # To take input from user without echoing.

####################################################################################
## GET Login Details from User - Target Device IP, Username, Password ##############
####################################################################################
get_ip = input(str("Please type IP or Hostname of the target device: "))
get_user = input(str("Please enter your username: "))
passwd = getpass.getpass("Password: ")

####################################################################################
## Convert Username & Password to Base64 encoded value to supply as header #########
####################################################################################

auth_header = str(f"{get_user}:{passwd}")

base64_encode = base64.b64encode(auth_header.encode("utf-8"))
auth_header_value = str(base64_encode, "utf-8")

####################################################################################
## Collecting all information in one code block ####################################
####################################################################################
user = str.upper(get_user)
print(f"\nConnecting to the Target Device {get_ip} via username {user}.")

rtr = {"ip": get_ip, "port": "443"}

headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': f"Basic {auth_header_value}"}

url = f"https://{rtr['ip']}:{rtr['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"


####################################################################################
## Defining action that needs to be performed ######################################
####################################################################################

pull_response = requests.get(url, headers=headers, verify=False)

api_data = pull_response.json()
print("\n")
print('*' * 50)
pprint(api_data["Cisco-IOS-XE-interfaces-oper:interface"]["description"])
print('*' * 50)

if api_data["Cisco-IOS-XE-interfaces-oper:interface"]["admin-status"] == 'if-state-up':
    print("\nInterface is up!")
