# https://leetcode.com/problems/sort-an-array/
# 912. Sort an Array

import random


def sortArray(nums):
    """
        :type nums: List[int]
        :rtype: List[int]
    """

    def quick_sort(arr, left, right):
        if left >= right:
            return
        
        # Выбираем опорный элемент
        pivot_idx = random.randint(left, right)
        pivot = arr[pivot_idx]
        l, r = left, right

        # Перемещаем элементы меньше опорного влево, больше - вправо
        while l <= r:
            while arr[l] < pivot:
                l += 1
            while arr[r] > pivot:
                r -= 1
            if l <= r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1

        quick_sort(arr, left, r)
        quick_sort(arr, l, right)

    quick_sort(nums, 0, len(nums) - 1)
    return nums

nums = eval(input())
print(sortArray(nums))