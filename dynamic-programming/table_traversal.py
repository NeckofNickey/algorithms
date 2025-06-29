# https://informatics.msk.ru/mod/statements/view.php?id=84550&chapterid=206#1

def get_num_of_ways(m, n):
    
    matrix = [[0] * n for _ in range(m)]
    matrix[0][0] = 1
    
    for i in range(m):
        for j in range(n):
            if i >= 1:
                matrix[i][j] = matrix[i - 1][j]
            if j >= 1:
                matrix[i][j] = matrix[i][j - 1]
    
    return matrix[m - 1][n - 1]


m, n = map(int, input().split())
print(get_num_of_ways(m, n))