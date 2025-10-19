# https://informatics.msk.ru/mod/statements/view.php?id=53233&chapterid=114108#1
# Диаметр дерева

import sys
sys.setrecursionlimit(300000)

def dfs(v, parent, depth, graph, dist):
    dist[v] = depth
    for neighbor in graph[v]:
        if neighbor != parent:
            dfs(neighbor, v, depth + 1, graph, dist)


data = sys.stdin.read().split()
n = int(data[0])

graph = [[] for _ in range(n + 1)]

idx = 1
for _ in range(n - 1):
    u, v = int(data[idx]), int(data[idx + 1])
    idx += 2
    graph[u].append(v)
    graph[v].append(u)

dist1 = [-1] * (n + 1)
# Первый DFS из вершины 1
dfs(1, -1, 0, graph, dist1)

# Находим самую удаленную вершину от 1
farthest = max(range(1, n + 1), key=lambda x: dist1[x])

dist2 = [-1] * (n + 1)
# Второй DFS из самой удаленной вершины
dfs(farthest, -1, 0, graph, dist2)

diameter = max(dist2[1:])
print(diameter)