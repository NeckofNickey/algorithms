# https://stepik.org/lesson/1489018/step/6?unit=1508912
# Сортировка вставками

def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
             arr[j + 1] = arr[j]
             j -= 1
        
        arr[j + 1] = key


array = list(map(int, input().split()))
insertion_sort(array)
print(array)