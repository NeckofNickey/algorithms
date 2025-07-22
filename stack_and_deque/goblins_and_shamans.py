# https://informatics.msk.ru/mod/statements/view.php?id=206&chapterid=112984#1
# Гоблины и шаманы

import sys
import math

def get_number_of_goblin(operations: list) -> list:
    
    deq = []
    
    queue = []
    
    index = 0
    
    while operations and index < len(operations):
        
        if operations[index] == '+':
            deq.append(operations[index + 1])
            index += 2
        elif operations[index] == '*':
            mid = math.ceil(len(deq) / 2)
            first_part = deq[:mid]
            second_part = deq[mid:]
            first_part.append(operations[index + 1])
            deq = first_part + second_part
            index += 2
        elif operations[index] == '-':
            queue.append(deq.pop(0))
            index += 1
            
    return queue


data = sys.stdin.read().split()
index = 0
n = data[index]
index += 1
operations = data[index:]

result = get_number_of_goblin(operations)

sys.stdout.write('\n'.join(result))
