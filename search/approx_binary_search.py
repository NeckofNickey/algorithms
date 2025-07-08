# https://informatics.msk.ru/mod/statements/view.php?id=192&chapterid=2#1
# Приближенный двоичный поиск

def search_num_approx(num, array):
    
    if array[0] >= num:
        return array[0]
    elif array[-1] <= num:
        return array[-1]
    
    left = 0
    right = len(array) - 1
    
    while left <= right:
        
        mid = (left + right) // 2
        
        if array[mid] == num:
            return array[mid]
        elif array[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
            
    if abs(array[left] - num) < abs(array[right] - num):
        return array[left]
    else:
        return array[right]
            

n, k = map(int, input().split())
array = list(map(int, input().split()))
num_list = list(map(int, input().split()))

for num in num_list:
    print(search_num_approx(num, array))