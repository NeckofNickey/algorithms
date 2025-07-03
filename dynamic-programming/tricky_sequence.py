# https://informatics.msk.ru/mod/statements/view.php?id=649&chapterid=844#1

def get_n_seq(n):
    
    n_seq = [0] * (n + 2)
    n_seq[0] = n_seq[1] = 1
    
    for i in range(1, n // 2 + 1):
        if i * 2 <= n + 1:
            n_seq[i*2] = n_seq[i] + 1
        if i*2 + 2 <= n + 1:
            n_seq[i*2 + 2] = n_seq[(i*2 + 2) // 2] + 1
            n_seq[i*2 + 1] = n_seq[i*2 + 2] + n_seq[i]
    
    return n_seq[n]


n = int(input())
print(get_n_seq(n))