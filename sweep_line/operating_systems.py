# https://miro.com/app/board/uXjVJJ6SJsw=/
# Операционные системы
import heapq
import sys

def count_active_systems(n, partitions):
    
    # Создаем события 
    events = []
    for i, (a, b) in enumerate(partitions):
        events.append((a, 1, i + 1))
        events.append((b + 1, -1, i + 1))
    events.sort()

    # Обрабатываем события
    alive = [True] * n
    active = [] # max-heap по индексу -> используем отрицание
    active_set = set()

    ptr = 0
    # проходим по всем точкам в событиях
    while ptr < len(events):
        x = events[ptr][0]
        # обработка всех событий в точке x
        while ptr < len(events) and events[ptr][0] == x:
            _, event, idx = events[ptr]
            if event == 1:
                heapq.heappush(active, -idx)
                active_set.add(idx)
            else:
                active_set.discard(idx)
            ptr += 1
        
        # чистим heap от неактивных
        while active and (-active[0] not in active_set):
            heapq.heappop(active)

        # если есть активные — живёт только самый поздний
        if active:
            winner = -active[0]
            for idx in list(active_set):
                if idx != winner and alive[idx]:
                    alive[idx] = False
        
    return sum(alive)


data = sys.stdin.read().split()
m = int(data[0])
n = int(data[1])

partitions = []
for i in range(2, len(data), 2):
    partitions.append(list(map(int, data[i: i+2])))

print(count_active_systems(n, partitions))