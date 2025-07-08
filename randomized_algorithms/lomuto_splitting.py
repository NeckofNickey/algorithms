# https://new.contest.yandex.ru/contests/48570/problem?id=215%2F2023_04_06%2Fonaxya4yqZ
# Разбиение Ломуто

def get_lomuto_splitting(n, array):
    
    first_num = array[0]
    
    more_idx_start = 1
    more_idx_end = 1
    
    for i in range(1, n):
        if array[i] < first_num:
            array[i], array[more_idx_start] = array[more_idx_start], array[i]
            more_idx_end = i
            more_idx_start += 1
        else:
            more_idx_end = i
            
    array[0], array[more_idx_start - 1] = array[more_idx_start - 1], array[0]
  
    return array


n = int(input())
array = list(map(int, input().split()))

print(' '.join(map(str, get_lomuto_splitting(n, array))))