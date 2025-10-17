# https://informatics.msk.ru/mod/statements/view.php?id=256&chapterid=111540#1
# Компоненты связности

import sys
sys.setrecursionlimit(300000)

def dfs(v, graph, visited, component):
    visited[v] = True
    component.append(v + 1)
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, component)

def get_num_connectivity_components(vertex_num, graph):
    
    visited = [False] * vertex_num
    components = []


    for i in range(vertex_num):
        if not visited[i]:
            component = []
            dfs(i, graph, visited, component)
            components.append(component)

    return components


data = sys.stdin.read().split()
vertex_num = int(data[0])
edges_num = int(data[1])

graph = [[] for _ in range(vertex_num)]

idx = 2

for _ in range(edges_num):
    u = int(data[idx]) - 1
    v = int(data[idx + 1]) - 1
    idx += 2
    graph[u].append(v)
    graph[v].append(u)


components = get_num_connectivity_components(vertex_num, graph)


# Вывод результата
print(len(components))
for comp in components:
    print(len(comp))
    print(' '.join(map(str, sorted(comp))))


