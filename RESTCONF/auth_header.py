import base64
import requests
import json
from pprint import pprint
import getpass

get_ip = input(str("Please type IP or Hostname of the target device: "))
get_user = input(str("Please enter your username: "))
passwd = getpass.getpass("Password: ")

auth_header = str(f"{get_user}:{passwd}")

base64_encode = base64.b64encode(auth_header.encode("utf-8"))
auth_header_value = str(base64_encode, "utf-8")

print(auth_header_value)
