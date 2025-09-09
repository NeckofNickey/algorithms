# https://informatics.msk.ru/mod/statements/view.php?id=656&chapterid=946#1
# Ход конем

def get_num_of_ways(m, n):
    
    # Конь не может добраться, если доска слишком маленькая
    if m == 1 and n == 1:
        return 1
    if m < 1 or n < 1 or (m < 3 and n < 3):
        return 0
    
    matrix = [[0] * (n) for _ in range(m)]
    matrix[0][0] = 1
    
    for i in range(m):
        for j in range(n):
            if i >= 1 and j >= 2:
                matrix[i][j] += matrix[i - 1][j - 2]
            if i >= 2 and j >= 1:
                matrix[i][j] += matrix[i - 2][j - 1] 
    
    return matrix[m - 1][n - 1]


m, n = list(map(int, input().split()))
print(get_num_of_ways(m, n))