# https://informatics.msk.ru/mod/statements/view.php?id=359&chapterid=465#1
# От списка ребер к матрице смежности, неориентированный вариант

import sys

def convert_graph(m, edges_list):
    
    matrix = [[0] * m for _ in range(m)]

    for i, j in edges_list:
        matrix[i - 1][j - 1] = 1
        matrix[j - 1][i - 1] = 1

    return matrix


data = sys.stdin.read().split()
m = int(data[0])
edges_num = int(data[1])
edges_list = [[int(data[i]), int(data[i + 1])] for i in range(2, len(data), 2)]

matrix = convert_graph(m, edges_list)

for row in matrix:
    print(' '.join(map(str, row)))