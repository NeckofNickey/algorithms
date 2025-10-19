# https://informatics.msk.ru/mod/statements/view.php?id=256#1
# Обход в глубину

import sys

def dfs(matrix, vertex, visited):

    if visited[vertex] == 1:
        return
    
    visited[vertex] = 1
    
    for i in range(len(matrix)):
        if matrix[vertex][i] == 1: 
            dfs(matrix, i, visited)


data = sys.stdin.read().split()
m = int(data[0])
vertex = int(data[1]) - 1
visited = [0] * m
matrix = []

for i in range(2, len(data), m):
    matrix.append(list(map(int, data[i: i + m])))

dfs(matrix, vertex, visited)

print(sum(visited))