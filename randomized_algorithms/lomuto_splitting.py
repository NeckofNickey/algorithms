# https://new.contest.yandex.ru/contests/48570/problem?id=215%2F2023_04_06%2Fonaxya4yqZ
# Разбиение Ломуто

def get_lomuto_splitting(n, array):
    
    pivot = array[0]
    split_index = 1
    
    for i in range(1, n):
        if array[i] < pivot:
            array[i], array[split_index] = array[split_index], array[i]
            split_index += 1
            
    array[0], array[split_index - 1] = array[split_index - 1], array[0]
  
    return array


n = int(input())
array = list(map(int, input().split()))

partitioned_array = get_lomuto_splitting(n, array)

print(' '.join(map(str, partitioned_array)))