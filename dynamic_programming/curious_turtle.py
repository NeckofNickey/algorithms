# https://informatics.msk.ru/mod/statements/view.php?id=86009#1
# Любопытная черепаха

import sys

def get_shortest_ways_num(m, n, field):

    # Считаем количество кратчайших путей для каждой точки на поле    
    dp_all_path = [[0] * n for _ in range(m)]
    dp_all_path[0][0] = 1

    for i in range(m):
        for j in range(n):
            if i > 0:
                dp_all_path[i][j] += dp_all_path[i - 1][j]
            if j > 0:
                dp_all_path[i][j] += dp_all_path[i][j - 1]

    # Считаем количество путей кратчайших путей, которые проходят только через нулевые точки
    dp_zero_path = [[0] * n for _ in range(m)]
    dp_zero_path[0][0] = 1

    for i in range(m):
        for j in range(n):
            if field[i][j] == 1:
                dp_zero_path[i][j] = 0
                continue
            if i > 0:
                dp_zero_path[i][j] += dp_zero_path[i - 1][j]
            if j > 0:
                dp_zero_path[i][j] += dp_zero_path[i][j - 1] 

    return dp_all_path[m - 1][n - 1] - dp_zero_path[m - 1][n - 1]

    
data = sys.stdin.read().split()
m, n = int(data[0]), int(data[1])
field = []
for i in range(2, len(data)):
    field.append(list(map(int, list(data[i]))))
print(get_shortest_ways_num(m, n, field))