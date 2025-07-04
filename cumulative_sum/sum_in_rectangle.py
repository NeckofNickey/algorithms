# https://informatics.msk.ru/mod/statements/view.php?id=67323&chapterid=2772#1

def get_cumsum_matrix(m, n, original_matrix):
    
    cumsum_matrix = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cumsum_matrix[i][j] = original_matrix[i - 1][j - 1] + cumsum_matrix[i - 1][j] + \
                                  cumsum_matrix[i][j - 1] - cumsum_matrix[i - 1][j - 1]
    
    
    return cumsum_matrix
    


m, n, k = tuple(map(int, input().split()))

original_matrix = [list(map(int, input().split())) for _ in range(m)]

cumsum_matrix = get_cumsum_matrix(m, n, original_matrix)

for _ in range(k):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    print(cumsum_matrix[x2][y2] - cumsum_matrix[x1 - 1][y2] - cumsum_matrix[x2][y1 - 1] + cumsum_matrix[x1 - 1][y1 - 1])

