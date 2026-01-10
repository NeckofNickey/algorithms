# https://new.contest.yandex.ru/contests/80784/problem?id=149944%2F2025_08_30%2FUTQXOVGmx4
# Перепад цен


import sys

def get_min_indexes(n, arr):
    
    if n <= 1:
        return None

    min_diff = float('inf')

    i, j = 0, 1

    left, right = 0, 1

    while right < n:
        if arr[left] - arr[right] < min_diff:
            i = left
            j = right
            min_diff = arr[left] - arr[right]
        if arr[right] < arr[left]:
            left = right
        right += 1

    return [i + 1, j + 1]


def get_max_indexes(n, arr):
    
    if n <= 1:
        return None

    max_diff = -float('inf')

    i, j = 0, 1

    left, right = 0, 1

    while right < n:
        if arr[left] - arr[right] > max_diff:
            i = left
            j = right
            max_diff = arr[left] - arr[right]
        if arr[right] > arr[left]:
            left = right
        right += 1

    return [i + 1, j + 1]
    

data = list(map(int, sys.stdin.read().split()))
n = data[0]
arr = data[1:]

min_indexes = get_min_indexes(n, arr)
max_indexes = get_max_indexes(n, arr)

print(" ".join(map(str, min_indexes)))
print(" ".join(map(str, max_indexes)))