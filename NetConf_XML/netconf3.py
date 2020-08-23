from ncclient import manager
import xml.dom.minidom
import xmltodict
from pprint import pprint

router = {"host": "10.10.20.48", "port": "830",
          "user": "developer", "pass": "C1sco12345"}

netconf_filter = """
    <filter>
     <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"> 
      <interface>
       <name>GigabitEthernet2</name>
      </interface>
     </interfaces>
     <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"> 
      <interface>
       <name>GigabitEthernet2</name>
      </interface>
     </interfaces-state>
    </filter>
"""

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
