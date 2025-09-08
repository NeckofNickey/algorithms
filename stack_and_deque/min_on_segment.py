# https://informatics.msk.ru/mod/statements/view.php?id=598&chapterid=756#1
# Минимум на отрезке - решением с помощью дека

from collections import deque
import sys


def get_min_on_segment(n, k, arr):
    
    dq = deque()
    result = []
    
    # Обрабатываем первые K элементов для формирования первого окна
    for i in range(k):
        # Удаляем из конца дека все элементы, которые >= текущего
        while dq and arr[dq[-1]] >= arr[i]:
            dq.pop()
        dq.append(i)
        
    # Обрабатываем остальные элементы
    for i in range(k, n):
        # Минимум текущего окна находится в начале дека
        result.append(str(arr[dq[0]]))
        
        # Удаляем индексы, которые вышли за левую границу окна
        # Текущее окно: [i - k + 1, i]
        if dq and dq[0] == i - k:
            dq.popleft()
            
        
        # Добавляем новый элемент i, поддерживая порядок в деке
        while dq and arr[dq[-1]] >= arr[i]:
            dq.pop()
        dq.append(i)
        
    result.append(str(arr[dq[0]]))
    
    return result


def get_data():
    
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    arr = list(map(int, data[2:2+n]))
    
    return n, k, arr


def main():    
    n, k, arr = get_data()
    result = get_min_on_segment(n, k, arr)
    
    print('\n'.join(result))


if __name__ == "__main__":
    main()