# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# 215. Kth Largest Element in an Array

import random

def findKthLargest(nums, k):

    def quick_select(arr, left, right, k_smallest):
        
        if left == right:
            return arr[left]
        
        # Выбираем опорный элемент
        pivot_index = random.randint(left, right)
        pivot = arr[pivot_index]

        # Помещаем опорный элемент в конец, чтобы дальше в цикле его не трогать
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        
        # Создаем индекс, который будет отслеживать индекс, куда нам нужно будет
        # поместить опорный элемент, чтобы слева от него были значения меньше,
        # а справа значения больше 
        store_index = left

        # Проходимся по всем элементам подмассива и если элемент подмассива меньше,
        # чем опорный, то store_index увеличиваем на 1. Если store_index индекс
        # отстает от i, то значит встречалось значение, которе больше опорного
        # и должно быть правее, поэтому мы свапаем с i
        for i in range(left, right):
            if arr[i] < pivot:
                arr[store_index], arr[i] = arr[i], arr[store_index]
                store_index += 1

        arr[store_index], arr[right] = arr[right], arr[store_index]

        if k_smallest == store_index:
            return arr[k_smallest]
        elif k_smallest < store_index:
            return quick_select(arr, left, store_index - 1, k_smallest)
        else:
            return quick_select(arr, store_index + 1, right, k_smallest)
        
    n = len(nums)
    k_smallest = n - k
    return quick_select(nums, 0, n - 1, k_smallest)


nums = eval(input())
k = int(input())
print(findKthLargest(nums, k))
