# https://informatics.msk.ru/mod/statements/view.php?id=359&chapterid=460#1
# Проверка на неориентированность

import sys

def check_disorientation(m, matrix):

    # Проверка диагонали (отсутствие петель)
    for i in range(m):
        if matrix[i][i] != 0:
            return "NO"

    # Проверка симметричности
    for i in range(0, m):
        for j in range(i + 1, m):
            if matrix[i][j] != matrix[j][i]:
                return "NO"
    
    return 'YES'




data = sys.stdin.read().split()
m = int(data[0])
matrix = []
for i in range(1, len(data), m):
    matrix.append(list(map(int,data[i: i + m])))

print(check_disorientation(m, matrix))
