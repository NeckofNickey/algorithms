# https://informatics.msk.ru/mod/book/view.php?id=488&forceview=1
# https://informatics.msk.ru/mod/statements/view.php?id=766&chapterid=1792#1

def get_lis(seq):
    
    n = len(seq)
    matrix = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    
    # Инициализация таблицы LIS
    for i in range(n + 1):
        matrix[i][0] = -float('inf')
        
    # Заполнение таблицы LIS
    for i in range(1, n + 1):
        x_i = seq[i - 1]
        for j in range(n + 1):
            if matrix[i - 1][j - 1] < x_i < matrix[i - 1][j]:
                matrix[i][j] = x_i
            else:
                matrix[i][j] = matrix[i - 1][j]
    
    # Находим максимальную длину подпоследовательности
    max_len = 0
    for j in range(n, 0, -1):
        if matrix[n][j] != float('inf'):
            max_len = j
            break
        
    # Восстанавливаем подпоследовательность
    lis = []
    current_len = max_len
    current_val = float('inf')
    for i in range(n, 0, -1):
        if matrix[i][current_len] < current_val and matrix[i][current_len] != matrix[i - 1][current_len]:
            lis.append(matrix[i][current_len])
            current_val = matrix[i][current_len]
            current_len -= 1
            
            
    return lis[::-1]

n = int(input())
seq = list(map(int, input().split()))
lis = get_lis(seq)
print(' '.join(map(str, lis)))