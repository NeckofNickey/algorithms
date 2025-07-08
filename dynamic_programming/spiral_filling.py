# https://informatics.msk.ru/mod/statements/view.php?id=88420&chapterid=111384#1

def get_spiral_filling_matrix(m, n):
    
    matrix = [[0] * n for _ in range(m)]
    
    top, bottom = 0, m - 1
    left, right = 0, n - 1
    
    num = 1
    
    while num <= m * n:
        # Итерируемся по столбцам вправо
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        # По текущей верхней строке нам больше не нужно итерироваться, ее исключаем    
        top += 1
        
        # Итерируемся по строкам вниз
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        # По текущему правому столбцу нам больше не нужно итерироваться, его исключаем
        right -= 1 
        
        # Итерируемся по столбцам влево
        if top <= bottom:
            for i in range (right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            # По текущей нижней строке нам больше не нужно итерироваться, ее исключаем
            bottom -= 1
        
        # Итерируемся по строкам вверх
        if left <= right:
            for i in range (bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            # По текущему левому столбцу нам больше не нужно итерироваться, его исключаем
            left += 1
    
    return matrix
            

def print_matrix(m, matrix):
    
    for i in range(m):
        print(''.join([str(x).rjust(4) for x in matrix[i]]))


m, n = list(map(int, input().split()))

matrix = get_spiral_filling_matrix(m, n)

print_matrix(m, matrix)