# https://new.contest.yandex.ru/contests/80789/problems?id=149944%2F2025_09_07%2FNESBWi9s6w
# Передача пакетов с балансировкой

import heapq
import sys

def solve(packeges, packeges_num, servers):

    result = []

    servers_heap = []

    for i in range(servers):
        servers_heap.append((0, i))

    heapq.heapify(servers_heap)

    for packege in packeges:
        
        server_time, server_idx = heapq.heappop(servers_heap)
        packege_time, proc_duration = packege
        
        proc_start = server_time if server_time > packege_time else packege_time

        result.append(proc_start + proc_duration)

        heapq.heappush(servers_heap, (proc_start + proc_duration, server_idx))
    
    return result


        


data = sys.stdin.read().split()
packeges_num, servers = int(data[0]), int(data[1])

packeges = []

for i in range(2, len(data), 2):
    packeges.append((int(data[i]), int(data[i+1])))

result = solve(packeges,packeges_num, servers)

print(' '.join(map(str, result)))