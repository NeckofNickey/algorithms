# https://informatics.msk.ru/mod/statements/view.php?id=88420&chapterid=112371#1


def get_saddle_points(m, n, matrix):
    
    if not matrix:
        return 0
    
    saddle_points_list = []
    
    str_idx = 0
    
    while str_idx < m - 1:
        
        min_num_in_str = float('inf')
        min_num_in_str_idx = 0
        
        max_num_in_column = float('-inf')
        max_num_in_column_idx = 0
        
        for j in range(n):
            if matrix[str_idx][j] < min_num_in_str:
                min_num_in_str = matrix[str_idx][j]
                min_num_in_str_idx = j
                
        for i in range(m):
            if matrix[i][min_num_in_str_idx] > max_num_in_column:
                max_num_in_column = matrix[i][min_num_in_str_idx]
                max_num_in_column_idx = i
        
        if min_num_in_str == max_num_in_column:
            saddle_points_list.append([max_num_in_column_idx + 1, min_num_in_str_idx + 1])
        
        str_idx += 1
                

    return saddle_points_list


def print_all_saddle_points(saddle_points_list):
    
    if not saddle_points_list:
        print('0')
    
    for i in range(len(saddle_points_list)):
        print(' '.join(list(map(str, saddle_points_list[i]))))

m, n = list(map(int, input().split()))
matrix = []

for _ in range(m):
    matrix.append(list(map(int, input().split())))
    
print_all_saddle_points(get_saddle_points(m, n, matrix))