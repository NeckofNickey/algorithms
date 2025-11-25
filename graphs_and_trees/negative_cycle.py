# https://informatics.msk.ru/mod/statements/view.php?id=102087&chapterid=180#1
# Цикл

import sys

def find_negative_cycle(n, graph):
    INF = 10**5
    dist = [0] * n
    parent = [-1] * n
    last_updated = -1

    for i in range(n):
        updated = False
        for u in range(n):
            for v in range(n):
                if graph[u][v] < INF:
                    if dist[v] > dist[u] + graph[u][v]:
                        dist[v] = dist[u] + graph[u][v]
                        parent[v] = u
                        updated = True
                        if i == n - 1:
                            last_updated = v
        if not updated:
            break

    
    if last_updated == -1:
        print("NO")
        return
    
    # Входим внутрь цикла
    x = last_updated
    for _ in range(n):
        x = parent[x]

    # Восстановление
    cycle = []
    curr = x
    while True:
        cycle.append(curr + 1)
        curr = parent[curr]
        if curr == x:
            break
    cycle.append(x + 1)

    cycle.reverse()

    print("YES")
    print(len(cycle))
    print(' '.join(map(str, cycle)))


data = sys.stdin.read().split()
n = int(data[0])

graph = []

for i in range(1, len(data), n):
    graph.append(list(map(int, data[i: i + n])))

find_negative_cycle(n, graph)

