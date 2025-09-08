# https://informatics.msk.ru/mod/statements/view.php?id=77802#1
# Без массивов

import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    
    def print_reverse(index):
        if index < n:
            print_reverse(index + 1)
            print(data[index + 1], end=' ' if index > 0 else '')
    
    print_reverse(0)

if __name__ == "__main__":
    main()