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

    # тут смотрим нули между единицами, их 6, значит вариантов 7: 111111, 111110, 111100, 111000, 110000, 100000, 000000

# Решение для конкретной задачи
get_mask("158.116.11.146", "158.116.0.0")