# https://informatics.msk.ru/mod/statements/view.php?id=193&chapterid=6#1
# Дейкстра: восстановление пути


import heapq 
import sys

def dijkstra(n, start, end, matrix):
    # Преобразуем матрицу в список смежности
    graph = [[] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            weight = matrix[i-1][j-1]
            if weight >= 0:  # Изменено: включаем нулевые веса
                graph[i].append((j, weight))
    
    # Массивы для алгоритма Дейкстры
    dist = [float('inf')] * (n + 1)
    prev = [-1] * (n + 1) # Для восстановления пути
    dist[start] = 0

    heap = [(0, start)]

    while heap:
        current_dist, u = heapq.heappop(heap)

        if current_dist > dist[u]:
            continue

        if u == end:
            break

        for v, weight in graph[u]:
            new_dist = current_dist + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(heap, (new_dist, v))

    # Восстанавливаем путь
    if dist[end] == float('inf'):
        return [-1]
    
    path = []
    current = end
    while current != -1:
        path.append(current)
        current = prev[current]

    return path[::-1]
    

data = sys.stdin.read().split()

n, s, f = map(int, data[:3])
matrix = []
idx = 3
for i in range(n):
        row = list(map(int, data[idx:idx + n]))
        matrix.append(row)
        idx += n

result = dijkstra(n, s, f, matrix)

if result == [-1]:
    print(-1)
else:
    # Выводим весь путь, а не result[1:-1]
    print(' '.join(map(str, result)))