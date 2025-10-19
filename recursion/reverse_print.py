# Разворот последовательности

import sys

def reverse_print():
    num = int(sys.stdin.readline())
    if num == 0:
        print(num)
        return
    
    reverse_print()
    print(num)

reverse_print()