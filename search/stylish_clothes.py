# https://informatics.msk.ru/mod/statements/view.php?id=77306#1
# Стильная одежда

import sys


def get_most_suitable_clothes(t_num, t_list, p_num, p_list):
    
    def approx_bin_search(num, arr):

        if arr[0] >= num:
            return arr[0]
        elif arr[-1] <= num:
            return arr[-1]
        
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == num:
                return arr[mid]
            elif arr[mid] > num:
                right = mid - 1
            else:
                left = mid + 1

        
        if abs(arr[left] - num) < abs(arr[right] - num):
            return arr[left]
        else:
            return arr[right]
        
    # itter_list, bin_list = (t_list, p_list) if t_num < p_num else (p_list, t_list)

    min_diff = float('inf')
    best_t, best_p = None, None

    for num in t_list:
        closest_num = approx_bin_search(num, p_list)
        if abs(closest_num - num) < min_diff:
            min_diff = abs(closest_num - num)
            best_t = num
            best_p = closest_num
    
    return best_t, best_p




data = sys.stdin.read().split()
t_num = int(data[0])
t_list = list(map(int, data[1:1 + t_num]))
p_num = int(data[1 + t_num])
p_list = list(map(int, data[2 + t_num:2 + t_num + p_num]))

print(' '.join(map(str, get_most_suitable_clothes(t_num, t_list, p_num, p_list))))