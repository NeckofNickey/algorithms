# https://stepik.org/lesson/1489019/step/2?unit=1508913
# Обход в глубину

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')
    
    
    for vertex in graph[start]:
        if vertex not in visited:
            dfs(graph, vertex, visited)
                
    
    # Пример графа
graph = {
    'A': {'B', 'C'},
    'B': {'D', 'E'},
    'C': {'F'},
    'D': set(),
    'E': {'F'},
    'F': set()
}

# Запуск DFS
dfs(graph, 'A')  # Output: A B D E F C