# https://informatics.msk.ru/mod/statements/view.php?id=265#1

def reverse_permutation(n_list):
    
    perm_reverse = [0] * (len(n_list) + 1)
    
    for index, perm in enumerate(n_list, start=1):
        perm_reverse[perm] = index
    
    return ' '.join([str(n) for n in perm_reverse[1:]])


n = int(input())
s_list = list(input().strip().split())
n_list = [int(s) for s in s_list]

print(reverse_permutation(n_list))

