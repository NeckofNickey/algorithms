# https://stepik.org/lesson/1489018/step/5?unit=1508912
# Сортировка кучей

def heapify(arr, n, i):
    
    """Преобразует поддерево с корнем в i в max-кучу."""
    
    largest = i # Инициализируем наибольший элемент как корень
    first = 2*i + 1
    second = 2*i + 2
    
    # Если левый дочерний элемент существует и больше корня
    if first < n and arr[largest] < arr[first]:
        largest = first
        
    # Если правый дочерний элемент существует и больше текущего наибольшего    
    if second < n and arr[largest] < arr[second]:
        largest = second
        
    # Если наибольший элемент не корень
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest) # Рекурсивно преобразуем затронутое поддерево


def heap_sort(arr):
    
    """Сортировка кучей (Heap Sort)."""
    
    n = len(arr)
    
    # Построение max-кучи (перегруппируем массив)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    # Один за другим извлекаем элементы из кучи
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # Перемещаем текущий корень в конец
        heapify(arr, i, 0) # Вызываем heapify на уменьшенной куче


array = list(map(int, input().split()))
heap_sort(array)
print(array)
