# https://new.contest.yandex.ru/contests/48570/problem?id=215%2F2023_04_06%2FqQS9a7rB0y
# Быстрая сортировка

import random

def quick_sort(array):
    
    n = len(array)
    
    if n <= 1:
        return array
    
    
    # выбираем случайный индекс
    random_index = random.randint(0, n - 1)
    
    # ставим на первое место для осуществления сортировки Ломуто
    array[0], array[random_index] = array[random_index], array[0]
    
    # сортируем алгоритмом Ломуто, чтобы разделить массив на меньше случайного числа и больше случайного числа
    pivot = array[0]
    split_index = 1
    
    for i in range(1, n):
        if array[i] < pivot:
            array[i], array[split_index] = array[split_index], array[i]
            split_index += 1
            
    array[0], array[split_index - 1] = array[split_index - 1], array[0]
    
    return quick_sort(array[:split_index - 1]) + [pivot] + quick_sort(array[split_index:])

    

n = int(input())
array = list(map(int, input().split()))
sorted_array = quick_sort(array)

print(' '.join(map(str, sorted_array)))