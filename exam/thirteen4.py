from ipaddress import ip_network

net = ip_network('112.208.0.0/255.255.128.0')

counter = 0

for ip in net:
    if bin(int(ip)).count("1") % 11 == 0:
        counter += 1

print(counter)