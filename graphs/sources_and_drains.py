# https://informatics.msk.ru/mod/statements/view.php?id=359&chapterid=474#1
# Истоки и стоки

import sys

def get_sources_and_drains(m, matrix):
    
    sources_list = []
    drain_list = []

    for i, row in enumerate(matrix):
        if sum(row) == 0:
            drain_list.append(i + 1)

        
    for i in range(m):
        for j in range(m):
            if matrix[j][i] == 1:
                break
            elif j == (m - 1):
                sources_list.append(i + 1)

    return sources_list, drain_list



data = sys.stdin.read().split()
m = int(data[0])
matrix = []

for i in range(1, len(data), m):
    matrix.append(list(map(int, data[i: i + m])))


sources_list, drain_list = get_sources_and_drains(m, matrix)

print(len(sources_list))
print('\n'.join(map(str, sources_list)))
print(len(drain_list))
print('\n'.join(map(str, drain_list)))