# https://informatics.msk.ru/mod/statements/view.php?id=206&chapterid=112984#1
# Гоблины и шаманы

import sys
from collections import deque

def get_number_of_goblin(operations: list) -> list:
    
    left = deque()
    right = deque()
    
    queue = []
    
    index = 0
    
    while operations and index < len(operations):
        
        if operations[index] == '+':
            right.append(operations[index + 1])
            # Балансировка
            if len(right) > len(left):
                left.append(right.popleft())
            index += 2
        elif operations[index] == '*':
            right.appendleft(operations[index + 1])
            # Балансировка
            if len(right) > len(left):
                left.append(right.popleft())
            index += 2
        elif operations[index] == '-':
            queue.append(left.popleft())
            # Балансировка
            if len(left) < len(right):
                left.append(right.popleft())
            index += 1
            
    return queue


data = sys.stdin.read().split()
index = 0
n = data[index]
index += 1
operations = data[index:]

result = get_number_of_goblin(operations)

sys.stdout.write('\n'.join(result))
