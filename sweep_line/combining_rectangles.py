# https://miro.com/app/board/uXjVJJ6SJsw=/
# Объединение прямоугольников

import sys

def area_of_union(rectangles):

    if not rectangles:
        return 0
    
    # Собираем все уникальные x-координаты
    x_coords = set()
    for x1, y1, x2, y2 in rectangles:
        x_coords.add(x1)
        x_coords.add(x2)

    # Сортируем x-координаты
    xs = sorted(x_coords)

    total_area = 0

    # Проходим по всем промежуткам между x-координатами
    for i in range(len(xs) - 1):
        x_left = xs[i]
        x_right = xs[i + 1]
        if x_left == x_right:
            continue

        # Находим все прямоугольники, которые пересекают текущую вертикальную полосу
        active_intervals = []
        for x1, y1, x2, y2 in rectangles:
            if x1 <= x_left and x_right <= x2:
                active_intervals.append((y1, y2))

        if not active_intervals:
            continue

        # Объединяем y-интервалы
        active_intervals.sort()
        merged = []
        current_start, current_end = active_intervals[0]

        for start, end in active_intervals[1:]:
            if start <= current_end:
                current_end = max(end, current_end)
            else:
                merged.append((current_start, current_end))
                current_start, current_end = start, end
        merged.append((current_start, current_end))

        # Суммируем длины y-интервалов
        y_length = 0
        for start, end in merged:
            y_length += (end - start)

        # Добавляем площадь текущей вертикальной полосы
        total_area += y_length * (x_right - x_left)

    return total_area
    

data = sys.stdin.read().split()
n = int(data[0])
rectangles = []
for i in range(1, len(data), 4):
    x1 = int(data[i])
    y1 = int(data[i + 1])
    x2 = int(data[i + 2])
    y2 = int(data[i + 3])
    rectangles.append((x1, y1, x2, y2))

print(area_of_union(rectangles))