# https://informatics.msk.ru/mod/statements/view.php?id=766&chapterid=1792#1



def get_lis_with_recovery(seq):
    
    if not seq:
        return 0
    
    max_seq = [1] * len(seq)
    
    for i in range(1, len(seq)):
        for j in range(i):
            if seq[j] < seq[i]:
                max_seq[i] = max(max_seq[i], max_seq[j] + 1)
                
    return max(max_seq)

                
n = int(input())
seq = list(map(int, input().split()))
print(get_lis_with_recovery(seq))