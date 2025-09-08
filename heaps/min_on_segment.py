# https://informatics.msk.ru/mod/statements/view.php?id=598&chapterid=756#1
# Минимум на отрезке

import heapq
from collections import defaultdict
import sys

def get_min_on_segment(n, k, arr):
    
    # Создаем минимальную кучу
    heap = []
    # Словарь для отслеживания "удаленных" элементов (ленивое удаление)
    removed = defaultdict(int)
    result = []
    
    # Инициализация: добавляем первые K элементов в кучу
    for i in range(k):
        heapq.heappush(heap, arr[i])
    
    # Первый минимум
    result.append(str(heap[0]))
    
    # Обрабатываем остальные элементы
    for i in range(k, n):
        # Помечаем элемент, который выходит из окна, для удаления
        left_element = arr[i - k]
        removed[left_element] += 1
        
        # Добавляем новый элемент
        heapq.heappush(heap, arr[i])
        
        # Удаляем "недействительные" элементы с вершины кучи
        while heap and removed.get(heap[0], 0) > 0:
            elem = heapq.heappop(heap)
            removed[elem] -= 1
            if removed[elem] == 0:
                del removed[elem]
        
        # Минимум текущего окна - на вершине кучи
        result.append(str(heap[0]))
        
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