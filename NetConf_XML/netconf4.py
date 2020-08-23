from ncclient import manager
import xml.dom.minidom
import xmltodict
from pprint import pprint
from routers_info import router


netconf_filter = open("netconf_filter.xml").read()

with manager.connect(host=router["host"], port=router["port"], username=router["user"], password=router["pass"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)

    print(f"Connected to {router['host']}!")
    interface_netconf = m.get(netconf_filter)
    print("Getting Running Configuration...\n")

interface_python = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
pprint(interface_python)
name = interface_python['interfaces']['interface']['name']['#text']
print(name)
print("\n")
print("Closing Connection!")

config = interface_python["interfaces"]["interface"]
op_state = interface_python["interfaces-state"]["interface"]

print("Start")
print(f"Name: {config['name']['#text']}")
print(f"Description: {config['description']}")
print(f"Packets In {op_state['statistics']['in-unicast-pkts']}")
