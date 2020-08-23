from ncclient import manager
from routers_info import router

config_template = open('ios_config.xml').read()

netconfig_config = config_template.format(
    inf_name="GigabitEthernet2", inf_desc="AVILABS, Inc.")

with manager.connect(host=router["host"], port=router["port"], username=router["user"], password=router["pass"], hostkey_verify=False) as m:
    device_reply = m.edit_config(netconfig_config, target='running')
    print(device_reply)
    m.close_session()
