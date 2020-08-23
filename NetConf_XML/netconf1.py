from ncclient import manager

router = {"host": "ios-xe-mgmt-latest.cisco.com", "port": "10000",
          "user": "developer", "pass": "C1sco12345"}

with manager.connect(host=router["host"], port=router["port"], username=router["user"], password=router["pass"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)
    m.close_session()
