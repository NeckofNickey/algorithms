# https://informatics.msk.ru/mod/statements/view.php?id=77938&chapterid=112595#1
# Множества и подмножества

import sys

def get_pairs(n):
    
    pairs = []
    subset = n
    while True:
        z = n ^ subset  # Z - это X без элементов Y
        pairs.append((subset, z))
        if subset == 0:
            break
        subset = (subset - 1) & n  # следующий поднабор X
        
    pairs.sort()  # по возрастанию сначала по Y, потом по Z
    
    return pairs


line = sys.stdin.readline()
if line.strip():  # защищаемся от пустого ввода
    n = int(line)
    pairs_list = get_pairs(n)
    sys.stdout.write('\n'.join(f'{y} {z}' for y, z in pairs_list) + '\n')