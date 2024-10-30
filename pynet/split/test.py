import ipaddress

try:
    network = ipaddress.ip_network('177.126.37.0/23')
    print("Valid CIDR block:", network)
except ValueError as e:
    print("Error:", e)
