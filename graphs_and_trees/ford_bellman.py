# https://informatics.msk.ru/mod/statements/view.php?id=102087&chapterid=178#1
# Форд-Беллман

import sys

def get_distance(n, edges):
    
    INF = 30000
    dist = [INF] * (n + 1)
    dist[1] = 0

    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] < INF:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
        if not updated:
            break

    return dist[1:]


data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])

edges = []

for i in range(2, len(data), 3):
    edges.append(list(map(int, data[i: i + 3])))

distance = get_distance(n, edges)

print(' '.join(map(str, distance)))


