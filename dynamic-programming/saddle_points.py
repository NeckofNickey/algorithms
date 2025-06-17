# https://informatics.msk.ru/mod/statements/view.php?id=88420&chapterid=112371#1

def get_min_index_in_list(num_list):
    
    if not num_list:
        return None
    
    
    min_index = None
    min_num = float('inf')
    
    for i in range(len(num_list)):
        if num_list[i] < min_num:
            min_num = num_list[i]
            min_index = i
    
    return min_index


def get_max_index_in_list(num_list):
    
    if not num_list:
        return None
    
    
    max_index = None
    max_num = float('-inf')
    
    for i in range(len(num_list)):
        if num_list[i] > max_num:
            max_num = num_list[i]
            max_index = i
    
    return max_index


def get_saddle_points(m, n, matrix):
    
    saddle_points_list = []
    
    min_string_list = [get_min_index_in_list(num_list) for num_list in matrix]
    max_column_list = []
    
    
    

    return saddle_points_list

m, n = list(map(int, input().split()))
matrix = []

for _ in range(m):
    matrix.append(list(map(int, input().split())))
    
print(' '.join(get_saddle_points(m, n, matrix)))