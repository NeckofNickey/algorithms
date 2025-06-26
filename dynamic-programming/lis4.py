# https://informatics.msk.ru/mod/book/view.php?id=488&forceview=1
# https://informatics.msk.ru/mod/statements/view.php?id=766&chapterid=1792#1

def find_lis(sequence):
    
    if not sequence:
        return []
    
    n = len(sequence)
    # Массив для хранения минимальных окончаний подпоследовательностей разной длины
    min_tails = [float('inf')] * (n + 1)
    min_tails[0] = float('-inf')  # Базовый случай
    
    # Массивы для восстановления последовательности
    predecessor = [-1] * n  # Индексы предшественников
    indices = [0] * n       # Длины LIS для каждого элемента
    
    for i in range(n):
        # Бинарный поиск вручную
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if min_tails[mid] < sequence[i]:
                left = mid + 1
            else:
                right = mid - 1
        
        pos = left
        # Обновляем минимальное окончание для этой длины
        if sequence[i] < min_tails[pos]:
            min_tails[pos] = sequence[i]
        
        # Сохраняем информацию для восстановления
        indices[i] = pos
        if pos > 1:
            # Ищем предыдущий элемент в LIS
            for j in range(i-1, -1, -1):
                if sequence[j] < sequence[i] and indices[j] == pos - 1:
                    predecessor[i] = j
                    break
    
    # Находим длину LIS
    max_len = 0
    for i in range(n, 0, -1):
        if min_tails[i] != float('inf'):
            max_len = i
            break
    
    # Восстанавливаем LIS
    lis = []
    # Находим последний элемент LIS
    last_idx = -1
    for i in range(n):
        if indices[i] == max_len:
            last_idx = i
            break
    
    # Собираем последовательность
    while last_idx != -1:
        lis.append(sequence[last_idx])
        last_idx = predecessor[last_idx]
    
    return lis[::-1]  # Разворачиваем, так как добавляли с конца

# Чтение входных данных
n = int(input())
sequence = list(map(int, input().split()))

# Поиск и вывод LIS
lis = find_lis(sequence)
print(' '.join(map(str, lis)))