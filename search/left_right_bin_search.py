# https://informatics.msk.ru/mod/statements/view.php?id=192&chapterid=111728#1
# Левый и правый двоичный поиск

def get_left_idx(num, array):
    
    left = 0
    right = len(array) - 1
    
    result_left_idx = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if num == array[mid]:
            result_left_idx = mid
            right = mid - 1
        elif num > array[mid]:
            left = mid + 1
        else: 
            right = mid - 1

    return result_left_idx + 1 if result_left_idx != -1 else 0


def get_right_idx(num, array):
    
    left = 0
    right = len(array) - 1
    
    result_right_idx = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if num == array[mid]:
            result_right_idx = mid
            left = mid + 1
        elif num > array[mid]:
            left = mid + 1
        else: 
            right = mid - 1

    return result_right_idx + 1 if result_right_idx != -1 else 0


n, m = map(int, input().split())
array = list(map(int, input().split()))
num_list = list(map(int, input().split()))

for num in num_list:
    left = get_left_idx(num, array)
    right = get_right_idx(num, array)
    
    if left == 0 and right == 0:
        print(0)
    else:
        print(left, right)