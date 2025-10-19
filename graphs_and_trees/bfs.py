# https://stepik.org/lesson/1489019/step/2?unit=1508913
# Обход в ширину

from collections import deque

def bfs(graph, start):
    
    visited = set()
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)


# Граф, представленный в виде смежных вершин
graph = {
    'A': {'B', 'C'},
    'B': {'D', 'E'},
    'C': {'F'},
    'D': set(),
    'E': {'F'},
    'F': set()
}

# Запуск BFS с вершины 'A'
bfs(graph, 'A')