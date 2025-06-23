# https://informatics.msk.ru/mod/statements/view.php?id=766&chapterid=1792#1

def get_lis(seq):
    
    if not seq:
        return []
    
    # Шаг 1: Сортируем и удаляем дубликаты
    sorted_uniq_seq = []
    prev = None
    for num in sorted(seq):
        if num != prev:
            sorted_uniq_seq.append(num)
            prev = num
        
    # Шаг 2: Находим НОП между seq и sorted_unique
    m, n = len(seq), len(sorted_uniq_seq)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq[i - 1] == sorted_uniq_seq[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Шаг 3: Восстанавливаем подпоследовательность
    lis = []
    i, j = m, n
    
    while i > 0 and j > 0:
        if seq[i - 1] == sorted_uniq_seq[j-1]:
            lis.append(seq[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
            
    return lis[::-1]
    

n = int(input())
seq = list(map(int, input().split()))
lis = get_lis(seq)
print(' '.join(map(str, lis)))

# 3 29 5 5 28 6
# 3 5  5 6 28 29