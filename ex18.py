#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass

cisco1 = {
    "device_type": "cisco_ios",
    "host": "localhost",
    # 'port': 2222,
    "username": "pyclass",
    "password": getpass()
}

# Show command that we execute
command = "ls"
with ConnectHandler(**cisco1) as net_connect:
    output = net_connect.send_command(command)

# Automatically cleans-up the output so that
# only the show output is returned
print()
print(output)
print()