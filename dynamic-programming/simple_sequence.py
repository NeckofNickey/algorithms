def get_n_seq(n):
    
    n_seq = [0] * (n + 1) 
    n_seq[0] = n_seq[1] = 1 
    
    for i in range(1, n // 2 + 1):
        if i * 2 <= n:
            n_seq[i*2] = n_seq[i] + n_seq[i - 1]
        if i * 2 + 1 <= n:
            n_seq[i*2 + 1] = n_seq[i] - n_seq[i - 1]
    
    return n_seq[n]
    

n = int(input())
print(get_n_seq(n))