# https://informatics.msk.ru/mod/statements/view.php?id=193&chapterid=7#1
# Заправки

import heapq
import sys


def get_route_cost(n, prices, graph):
    
    # dist[i] - минимальная стоимость достижения города i
    dist = [float('inf')] * (n + 1)
    dist[1] = 0  # В начальном городе стоимость 0
    
    pq = [(0, 1)]  # (стоимость, город)
    
    while pq:
        cost, u = heapq.heappop(pq)
        
        if cost > dist[u]:
            continue
            
        if u == n:
            return cost
        
        # Для каждого соседа: стоимость = стоимость до u + цена бензина в u
        for v in graph[u]:
            new_cost = cost + prices[u]  # Покупаем бензин в u для переезда в v
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(pq, (new_cost, v))
    
    return -1


data = sys.stdin.read().split()

idx = 0
n = int(data[idx])
idx += 1
prices = [0] + list(map(int, data[idx:idx+n]))
idx += n
m = int(data[idx])
idx += 1

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u = int(data[idx])
    v = int(data[idx+1])
    idx += 2
    graph[u].append(v)
    graph[v].append(u)

result = get_route_cost(n, prices, graph)
print(result)




