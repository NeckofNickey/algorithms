from ipaddress import ip_network

# net = ip_network('192.168.32.160/255.255.255.240')

# for ip in net:
#     print(type(ip))

def get_mask(host_ip, network_ip):
    # Преобразуем IP в 32-битные числа
    h = sum(int(x) << (24 - 8*i) for i, x in enumerate(host_ip.split('.')))
    n = sum(int(x) << (24 - 8*i) for i, x in enumerate(network_ip.split('.')))

    print(bin(h))
    print(bin(n))

    # тут все просто: разбиваем на восьмерки и смотрим маску: 
    # 11111111.11111111.11110000.00000000

# Решение для конкретной задачи
get_mask("215.181.200.27", "215.181.192.0")