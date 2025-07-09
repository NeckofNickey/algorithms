# https://new.contest.yandex.ru/contests/48570/problem?id=215%2F2023_04_06%2FqQS9a7rB0y
# Быстрая сортировка

import random

def quick_sort(array):
    
    n = len(array)
    
    if n <= 1:
        return array
    
    
    # выбираем случайный индекс
    random_index = random.randint((n - 1) // 4, 3 * (n - 1) // 4)
    
    # ставим на первое место для осуществления сортировки Ломуто
    array[0], array[random_index] = array[random_index], array[0]
    
    # сортируем алгоритмом Ломуто, чтобы разделить массив на меньше случайного числа и больше случайного числа
    pivot = array[0]
    split_index = 1
    
    for i in range(1, n):
        if array[i] <= pivot:
            array[i], array[split_index] = array[split_index], array[i]
            split_index += 1
            
    array[0], array[split_index - 1] = array[split_index - 1], array[0]
    
    less_array = quick_sort(array[:split_index])
    more_array = quick_sort(array[split_index:])
    
    return get_merging_sequences(less_array, more_array)

  
def get_merging_sequences(list1, list2):
    
    # Осуществляем слияние
    sorted_array = []
    
    list1_idx = 0
    list2_idx = 0
    
    n_list1 = len(list1)
    n_list2 = len(list2)
    
    while list1_idx < n_list1 and list2_idx < n_list2:
        
        if list1[list1_idx] < list2[list2_idx]:
            sorted_array.append(list1[list1_idx])
            list1_idx += 1
        else:
            sorted_array.append(list2[list2_idx])
            list2_idx += 1
            
    sorted_array.extend(list1[list1_idx:])
    sorted_array.extend(list2[list2_idx:])
    
    return sorted_array
    

n = int(input())
array = list(map(int, input().split()))
sorted_array = quick_sort(array)

print(' '.join(map(str, sorted_array)))