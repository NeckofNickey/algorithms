# http://informatics.msk.ru/mod/statements/view.php?chapterid=1755#1
# Таможня

import sys

def get_min_device(pairs):

    events = []

    for start, duration in pairs:
        end = start + duration
        events.append((start, 1))
        events.append((end, -1))

    events.sort()

    intersections = 0
    max_intersections = -float('inf')
    for _, event in events:
        if event > 0:
            intersections += 1
            max_intersections = max(max_intersections, intersections)
        else:
            intersections -= 1

    return max_intersections

data = sys.stdin.read().split()
n = int(data[0])

pairs = [(int(data[i]), int(data[i + 1])) for i in range(1, len(data), 2)]

print(get_min_device(pairs))