# https://informatics.msk.ru/mod/statements/view.php?id=656&chapterid=2962#1

def get_num_of_ways(m, n):
    
    matrix = [[0] * (n) for _ in range(m)]
    matrix[0][0] = 1
    
    for s in range(m + n - 1):
        # Определяем диапазон строк для текущей диагонали
        i_start = max(0, s - n + 1)
        i_end = min(s, m - 1)
        
        for i in range(i_start, i_end + 1):
            j = s - i
            if i >= 2 and j < n - 1:
                matrix[i][j] += matrix[i - 2][j + 1]
            if i >= 2 and j >= 1:
                matrix[i][j] += matrix[i - 2][j - 1]
            if i >= 1 and j >= 2:
                matrix[i][j] += matrix[i - 1][j - 2]
            if i < m - 1 and j >= 2:
                matrix[i][j] += matrix[i + 1][j - 2]
                    
    return matrix[m - 1][n - 1]


m, n = list(map(int, input().split()))
print(get_num_of_ways(m, n))