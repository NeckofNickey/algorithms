# https://new.contest.yandex.ru/contests/48558/problem?id=215%2F2023_04_06%2FHFqqJtCCRh

def is_win_stones(n, m):
    
    matrix = [['Win'] * (m + 1) for _ in range(n + 1)]
    
    matrix[0][0] = 'Lose'
    
    for i in range(1, n + 1):
        if i % 3 == 0:
            matrix[i][0] = 'Lose'
        else:
            matrix[i][0] = 'Win'
            
    for j in range(1, m + 1):
        if j % 3 == 0:
            matrix[0][j] = 'Lose'
        else:
            matrix[0][j] = 'Win'
            
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if matrix[i - 1][j - 1] == 'Lose':
                matrix[i][j] = 'Lose'
                
    
    return matrix[n][m]
            

n, m = list(map(int, input().split()))
print(is_win_stones(n, m))