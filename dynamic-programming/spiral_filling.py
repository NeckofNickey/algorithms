def get_spiral_filling_matrix(m, n):
    
    matrix = [[0] * n for _ in range(m)]
    
    string_top_idx = 0
    string_bottom_idx = m - 1
    column_left_idx = 0
    column_right_idx = n - 1
    
    string_idx = 0
    column_idx = 0
    
    num_in_matrix = 1
    
    while num_in_matrix <= m * n:
        if string_idx == string_top_idx and column_idx == column_left_idx:
            # Итерируемся по столбцам вправо
            while column_idx <= column_right_idx:
                matrix[string_idx][column_idx] = num_in_matrix
                column_idx += 1
                num_in_matrix += 1
            # По текущей верхней строке нам больше не нужно итерироваться, ее исключаем    
            string_top_idx += 1
            # Перескакиваем ниже
            string_idx += 1
            # Возвращаем индекс на место, так как в цикле выше он лишний раз увеличивается
            column_idx -= 1
            
        elif string_idx == string_top_idx and column_idx == column_right_idx:
            # Итерируемся по строкам вниз
            while string_idx <= string_bottom_idx:
                matrix[string_idx][column_idx] = num_in_matrix
                string_idx += 1
                num_in_matrix += 1
            # По текущему правому столбцу нам больше не нужно итерироваться, его исключаем
            column_right_idx -= 1 
            # Перескакиваем левее
            column_idx -= 1
            # Возвращаем индекс на место, так как в цикле выше он лишний раз увеличивается
            string_idx -= 1
            
        elif string_idx == string_bottom_idx and column_idx == column_right_idx:
            # Итерируемся по столбцам влево
            while column_idx >= column_left_idx:
                matrix[string_idx][column_idx] = num_in_matrix
                column_idx -= 1
                num_in_matrix += 1
            # По текущей нижней строке нам больше не нужно итерироваться, ее исключаем
            string_bottom_idx -= 1
            # Перескакиваем вверх
            string_idx -= 1
            # Возвращаем индекс на место, так как в цикле выше он лишний раз увеличивается
            column_idx += 1
                
        elif string_idx == string_bottom_idx and column_idx == column_left_idx:
            # Итерируемся по строкам вверх
            while string_idx >= string_top_idx:
                matrix[string_idx][column_idx] = num_in_matrix
                string_idx -= 1
                num_in_matrix += 1
            # По текущему левому столбцу нам больше не нужно итерироваться, его исключаем
            column_left_idx += 1
            # Перескакиваем вправо
            column_idx += 1
            # Возвращаем индекс на место, так как в цикле выше он лишний раз увеличивается
            string_idx += 1
    
    return matrix
            

def print_matrix(m, matrix):
    
    for i in range(m):
        print(''.join([str(x).rjust(4) for x in matrix[i]]))


m, n = list(map(int, input().split()))

matrix = get_spiral_filling_matrix(m, n)

print_matrix(m, matrix)