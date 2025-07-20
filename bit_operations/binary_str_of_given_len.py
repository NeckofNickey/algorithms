# https://informatics.msk.ru/mod/statements/view.php?id=77938&chapterid=80#1
# Двоичные строки заданной длины

import sys

def get_binary_str(n):
    
    binary_str_list = []
    
    for num in range(2**n):
        binary_str_list.append(f'{num:0{n}b}')
        
    return binary_str_list


n = int(input())
result_list = get_binary_str(n)
sys.stdout.write('\n'.join(result_list))