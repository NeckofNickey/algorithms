# http://informatics.msk.ru/mod/statements/view.php?id=102087#1
# Флойд - 1

import sys

def get_best_matrix(n, graph):
    
    dist = [[0] * n for _ in range(n)]

    # Копируем исходный граф в матрицу расстояний
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            else:
                dist[i][j] = graph[i][j]

    # Алгоритм Флойда-Уоршелла
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
    

data = sys.stdin.read().split()
n = int(data[0])

graph = []
for i in range(1, len(data), n):
    graph.append(list(map(int, data[i: i + n])))

result = get_best_matrix(n, graph)

for i in range(n):
    print(' '.join(map(str, result[i])))
