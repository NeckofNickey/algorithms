# https://informatics.msk.ru/mod/statements/view.php?id=77938&chapterid=112595#1
# Множества и подмножества

import sys

def get_pairs(n):
    
    pairs_list = []
    
    for num in range(n + 1):
        if (num & n) == num and (num & (n - num)) == 0:
            pairs_list.append(f'{num} {n - num}')
    
    return pairs_list


n = int(sys.stdin.readline())
pairs_list = get_pairs(n)

sys.stdout.write('\n'.join(pairs_list))