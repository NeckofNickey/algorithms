# https://informatics.msk.ru/mod/statements/view.php?id=256&chapterid=165#1
# Банкет


import sys

def dfs(v, color, graph, colors):
    colors[v] = color
    for neighbor in graph[v]:
        if colors[neighbor] == color:
            return False
        if colors[neighbor] == 0:
            if not dfs(neighbor, 3 - color, graph, colors):
                return False
    
    return True



data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])

graph = [[] for _ in range(n + 1)]

idx = 2
for _ in range(m):
    u, v = int(data[idx]), int(data[idx + 1])
    idx += 2
    graph[u].append(v)
    graph[v].append(u)

colors = [0] * (n + 1) # 0 - не посещена, 1 и 2 - цвета

# Проверяем двудольность
for i in range(1, n + 1):
    if colors[i] == 0:
        if not dfs(i, 1, graph, colors):
            print("NO")
            sys.exit()
        
# Собираем вершины первого цвета
table1 = [i for i in range(1, n + 1) if colors[i] == 1]

print("YES")
print(' '.join(map(str, table1)))

