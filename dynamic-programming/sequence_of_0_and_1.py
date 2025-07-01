# https://informatics.msk.ru/mod/statements/view.php?id=654&chapterid=207#1

def get_num_of_seq(n):
    
    zero_end = [0] * n
    one_end = [0] * n
    
    zero_end[0] = 1
    one_end[0] = 1
    
    for i in range(1, n):
        zero_end[i] = zero_end[i - 1] + one_end[i - 1]
        one_end[i] = zero_end[i - 1]
        
    return zero_end[n - 1] + one_end[n - 1]
    
    
n = int(input())
print(get_num_of_seq(n))