# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/
# 632. Smallest Range Covering Elements from K Lists

import heapq

def smallestRange(nums):

    min_heap = []
    current_max = -float('inf')

    # Инициализация: первый элемент из каждой строки
    for i, arr in enumerate(nums):
        heapq.heappush(min_heap, (arr[0], i, 0))
        current_max = max(current_max, arr[0])

    result = [-float('inf'), float('inf')]

    while min_heap:
        current_min, list_idx, elem_idx = heapq.heappop(min_heap)

        # Обновляем результат
        if current_max - current_min < result[1] - result[0]:
            result = [current_min, current_max]

        # Если достигли конца какой-либо строки - выходим
        if elem_idx + 1 == len(nums[list_idx]):
            return result
        
        # Добавляем следующий элемент из той же строки
        next_val = nums[list_idx][elem_idx + 1]
        heapq.heappush(min_heap, (next_val, list_idx, elem_idx + 1))
        current_max = max(current_max, next_val)

    return result




# nums = eval(input())
nums = eval("[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]")
print(smallestRange(nums))