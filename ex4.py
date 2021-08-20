import ipaddress as ip

# netmask

net4 = ip.ip_network('10.0.1.0/24')
print(net4.netmask)