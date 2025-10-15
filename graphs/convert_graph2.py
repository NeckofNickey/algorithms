# https://informatics.msk.ru/mod/statements/view.php?id=359&chapterid=464#1
# От матрицы смежности к списку ребер, неориентированный вариант

import sys

def convert_graph(m, matrix):
    
    edges_list = []


    for i in range(m):
        if matrix[i][i] == 1:
            edges_list.append([matrix[i + 1][i + 1]])

    for i in range(0, m):
        for j in range(i + 1, m):
            if matrix[i][j] == 1:
                edges_list.append([i + 1, j + 1])

    return(edges_list)


data = sys.stdin.read().split()
m = int(data[0])
matrix = []

for i in range(1, len(data), m):
    matrix.append(list(map(int, data[i: i + m])))

edges_list = convert_graph(m, matrix)

for row in edges_list:
    print(' '.join(map(str, row)))