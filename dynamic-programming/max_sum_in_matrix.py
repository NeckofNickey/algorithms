def get_max_sum_in_matrix(m, n, matrix):
    
    max_sum = 0
    
    for i in range(m):
        for j in range(n):
            if i < m - 1: 
                max_sum = max(max_sum, matrix[i][j] + matrix[i + 1][j])
            if j < n - 1:
                max_sum = max(max_sum, matrix[i][j] + matrix[i][j + 1])
    
    return max_sum
                
            
m, n = list(map(int, input().split()))
matrix = []

for _ in range (m):
    matrix.append(list(map(int, input().split())))
    
print(get_max_sum_in_matrix(m, n, matrix))