# https://new.contest.yandex.ru/contests/48558/problem?id=215%2F2023_04_06%2FlX20wNIqZg

def is_win_stones(n, m):
    
    matrix = [[0] * (m + 1) for _ in range(n + 1)]
    
    matrix[0][0] = 'Lose'
    
    for i in range(1, n + 1):
        if matrix[i - 1][0] == 'Lose':
            matrix[i][0] = 'Win'
        else:
            matrix[i][0] = 'Lose'
            
    for j in range(1, m + 1):
        if matrix[0][j - 1] == 'Lose':
            matrix[0][j] = 'Win'
        else:
            matrix[0][j] = 'Lose'
            
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if matrix[i][j - 1] == 'Win' and matrix[i - 1][j - 1] == 'Win' and matrix[i - 1][j] == 'Win':
                matrix[i][j] = 'Lose'
            else:
                matrix[i][j] = 'Win'
    
    return matrix[n][m]

n, m = list(map(int, input().split()))
print(is_win_stones(n, m))