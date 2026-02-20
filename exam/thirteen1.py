from ipaddress import ip_network

# net = ip_network('192.168.32.160/255.255.255.240')

# for ip in net:
#     print(type(ip))

def min_zeros_in_mask(host_ip, network_ip):
    # Преобразуем IP в 32-битные числа
    h = sum(int(x) << (24 - 8*i) for i, x in enumerate(host_ip.split('.')))
    n = sum(int(x) << (24 - 8*i) for i, x in enumerate(network_ip.split('.')))

    print(bin(h))
    print(bin(n))
    
    return (h ^ n).bit_length()

# Решение для конкретной задачи
print(min_zeros_in_mask("111.91.200.28", "111.91.192.0"))