# https://informatics.msk.ru/mod/statements/view.php?id=77938&chapterid=113573#1
# Миссия джедая Ивана

import sys

def get_numbers(n, matrix):
    
    num_list = []
    
    for i in range(n):
        num = 0
        for j in range(n):
          num |= matrix[i][j]
        num_list.append(num)
        
    return num_list  
          


data= sys.stdin.read().split()
n = int(data[0])

matrix = []
start = 1
end = n + 1

for _ in range(n):
    matrix.append(list(map(int, data[start: end])))
    start = end
    end = end + n

num_list = get_numbers(n, matrix)

print(' '.join(map(str, num_list)))