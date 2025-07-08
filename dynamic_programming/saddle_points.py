# https://informatics.msk.ru/mod/statements/view.php?id=88420&chapterid=112371#1


def get_saddle_points(m, n, matrix):
    
    if not matrix:
        return 0
    
    saddle_points_list = []
    
    for i in range(m):
        # Находим минимальный элемент в строке и его индексы
        min_in_row = min(matrix[i])
        min_cols_idx_list = [j for j in range(n) if matrix[i][j] == min_in_row]
        
        for j in min_cols_idx_list:
            # Проверяем, является ли этот элемент максимальным в столбце
            column = [matrix[k][j] for k in range(m)]
            if matrix[i][j] == max(column):
                saddle_points_list.append((i + 1, j + 1))

    return saddle_points_list if saddle_points_list else 0


def print_all_saddle_points(saddle_points_list):
    
    if saddle_points_list == 0:
        print(0)
    else:
        for saddle_point in saddle_points_list:
            print(' '.join(list(map(str, saddle_point))))

m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]

    
print_all_saddle_points(get_saddle_points(m, n, matrix))