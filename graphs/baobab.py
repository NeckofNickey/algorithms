# https://informatics.msk.ru/mod/statements/view.php?id=256&chapterid=111541#1
# Баобаб
# Граф является деревом, если он связный и не содержит циклов (число рёбер = число вершин − 1).


import sys


def dfs(v, graph, visited):

    visited[v] = True

    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited)


def is_tree(m, matrix):
     
     # Подсчет рёбер
    edges = 0
    graph = [[] for _ in range(m)]

    for i in range(m):
        for j in range(i + 1, m):
            if matrix[i][j] == 1:
                edges += 1
                graph[i].append(j)
                graph[j].append(i)

    # Проверка условия m = n - 1
    if edges != m - 1:
         return "NO"
    
    # Проверка связности DFS
    visited = [False] * m
    dfs(0, graph, visited)

    return "YES" if all(visited) else "NO"

    
data = sys.stdin.read().split()
m = int(data[0])

matrix = []
for i in range(1, len(data), m):
    matrix.append(list(map(int, data[i: i + m])))


print(is_tree(m, matrix))

