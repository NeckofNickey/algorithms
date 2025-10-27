# https://informatics.msk.ru/mod/statements/view.php?chapterid=480#1
# Транзитивность ориентированного графа

import sys


def is_transitive(n, matrix):
    
    for u in range(n):
        for v in range(n):
            if matrix[u][v] == 1:
                for w in range(n):
                    if matrix[v][w] == 1:
                        if matrix[u][w] != 1:
                            return "NO"
                        
    
    return "YES"
                            


data = sys.stdin.read().split()

n = int(data[0])

matrix = []
for i in range(1, len(data), n):
    matrix.append(list(map(int, data[i: i + n])))

print(is_transitive(n, matrix))