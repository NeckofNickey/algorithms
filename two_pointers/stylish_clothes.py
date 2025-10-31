# https://informatics.msk.ru/mod/statements/view.php?id=77306#1
# Стильная одежда

import sys

def get_most_suitable_clothes(t_num, t_list, p_num, p_list):
    
    t_point, p_point = 0, 0
    min_diff = float('inf')
    best_pair = [None, None]

    while t_point < t_num and p_point < p_num:
        curr_diff = abs(t_list[t_point] - p_list[p_point]) 
        if curr_diff < min_diff:
            min_diff = curr_diff
            best_pair[0] = t_list[t_point]
            best_pair[1] = p_list[p_point] 
        if t_list[t_point] < p_list[p_point]:
            t_point += 1
        else:
            p_point += 1
    
    return best_pair


data = sys.stdin.read().split()
t_num = int(data[0])
t_list = list(map(int, data[1:1 + t_num]))
p_num = int(data[1 + t_num])
p_list = list(map(int, data[2 + t_num:2 + t_num + p_num]))

print(' '.join(map(str, get_most_suitable_clothes(t_num, t_list, p_num, p_list))))