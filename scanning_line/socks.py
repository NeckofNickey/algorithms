# https://informatics.msk.ru/mod/statements/view.php?chapterid=1429#1
# Носки

import sys

def get_thickness(l, n, m, socks, points):
    
    events = [0] * (l + 2)

    # Расставляем события
    for start, end in socks:
        events[start] += 1
        events[end + 1] -= 1

    # Считаем префиксную сумму
    current_sum = 0
    prefix_sum = [0] * (l + 1)
    for i in range(1, l + 1):
        current_sum += events[i]
        prefix_sum[i] = current_sum

    # Смотрим для каждой точки толщину
    thickness = []
    for point in points:
        thickness.append(prefix_sum[point])

    return thickness


data = sys.stdin.read().split()
l, n, m = int(data[0]), int(data[1]), int(data[2])

socks = [(int(data[i]), int(data[i + 1])) for i in range(3, 3 + (n * 2), 2)]

points = [(int(data[i])) for i in range(3 + (n * 2), len(data))]

thickness = get_thickness(l, n, m, socks, points)

print('\n'.join(map(str, thickness)))
