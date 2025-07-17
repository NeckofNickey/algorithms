# https://informatics.msk.ru/mod/statements/view.php?id=81344&chapterid=208#1
# Восстановление скобок

def get_restoring_ways(template):
    
    n = len(template)
    
    matrix = [[0] * (n + 3) for _ in range(n + 1)]
    matrix[0][1] = 1
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if template[i - 1] == '(':
                matrix[i][j] = matrix[i - 1][j - 1]
            elif template[i - 1] == ')':
                matrix[i][j] = matrix[i - 1][j + 1]
            elif template[i - 1] == '?':
                matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j + 1]
                
    return matrix[n][1]


template = input().strip()
print(get_restoring_ways(template))
