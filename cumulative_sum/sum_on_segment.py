# https://informatics.msk.ru/mod/statements/view.php?id=67323&chapterid=2771#1
# Сумма на отрезке

import sys

def get_cumsum_list(array):
    
    n = len(array)
    
    cumsum_list = [0] * (n + 1)

    for i in range(n):
        cumsum_list[i + 1] = cumsum_list[i] + array[i]

    return cumsum_list


data = sys.stdin.read().split()
a = int(data[0])
r = int(data[1])
array = list(map(int, data[2:2 + a]))

cumsum_list = get_cumsum_list(array)

result_list = []
for i in range(2 + a, a + 2 + 2 * r, 2):
    x = int(data[i])
    y = int(data[i + 1])
    result_list.append(str(cumsum_list[y] - cumsum_list[x - 1]))

sys.stdout.write('\n'.join(result_list))
    