# https://informatics.msk.ru/mod/statements/view.php?id=766#1

def get_lcs(m, n, m_seq, n_seq):
    
    length_matrix = [[0] * (n + 1) for _ in range(m+ 1)]
    
    for i in range (1, m + 1):
        for j in range(1, n + 1):
            if m_seq[i - 1] == n_seq[j - 1]:
                length_matrix[i][j] = length_matrix[i - 1][j - 1] + 1
            else:
                length_matrix[i][j] = max(length_matrix[i - 1][j], length_matrix[i][j - 1])
    
    # Восстановление последовательности          
    # lis = []           
    # i, j = m, n
    # while i > 0 and j > 0:
    #     if m_seq[i - 1] == n_seq[i - 1]:
    #         lis.append(m_seq[i - 1])
    #         i -= 1
    #         j -= 1
    #     elif length_matrix[i - 1][j] > length_matrix[i][j - 1]:
    #         i -= 1
    #     else:
    #         j -= 1
            
    # return lis[::-1]
    
    return length_matrix[m][n]


m = int(input())
m_seq = list(map(int, input().split()))
             
n = int(input())
n_seq = list(map(int, input().split()))

print(get_lcs(m, n, m_seq, n_seq))
