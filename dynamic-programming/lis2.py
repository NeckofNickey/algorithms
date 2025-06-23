# https://informatics.msk.ru/mod/statements/view.php?id=766&chapterid=1792#1


def get_lis(seq):
    
    n = len(seq)
    if n == 0:
        return []
    
    # Инициализация таблицы LIS
    LIS = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        LIS[i][0] = -float('inf')
    
    # Заполнение таблицы LIS
    for i in range(1, n + 1):
        x_i = seq[i - 1]
        for j in range(1, n + 1):
            if LIS[i - 1][j - 1] < x_i < LIS[i - 1][j]:
                LIS[i][j] = x_i
            else:
                LIS[i][j] = LIS[i - 1][j]
                
                
    lis = []
    for num in LIS[n]:
        if num != -float('inf') and num != float('inf'):
            lis.append(num)
    
    lis = lis[::-1]
    
    # # Находим максимальную длину подпоследовательности
    # max_len = 0
    # for j in range(n, 0, -1):
    #     if LIS[n][j] != float('inf'):
    #         max_len = j
    #         break
    
    # # Восстанавливаем подпоследовательность
    # lis = []
    # current_len = max_len
    # current_val = float('inf')
    
    # for i in range(n, 0, -1):
    #     if LIS[i][current_len] < current_val and LIS[i][current_len] != LIS[i - 1][current_len]:
    #         lis.append(LIS[i][current_len])
    #         current_val = LIS[i][current_len]
    #         current_len -= 1
    
    return lis[::-1]

                
n = int(input())
seq = list(map(int, input().split()))
lis = get_lis(seq)
print(' '.join(map(str, lis)))

# 3 1 4 1 5