def get_lis(seq):
    
    if not seq:
        return 0
    
    max_seq = []
    
    for i in range(len(seq)):
        for j in range(i):
            
            if seq[j] < seq[i]:
                pass

                
n = int(input())
seq = list(map(int, input().split()))
print(get_lis(seq))
