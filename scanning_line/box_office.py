# https://informatics.mccme.ru/mod/statements/view.php?chapterid=514#1
# Кассы

import sys

def get_intersect_time(intervals, intersect_factor):

    events = []

    for start, end in intervals:
        events.append((start, 1))
        events.append((end, -1))
    
    events.sort()


    intersect_time = 0
    intersections = 0
    current_start = 0
    is_start = False

    for time, event in events:
        intersections += event
        if intersections == intersect_factor and not is_start:
            is_start = True
            current_start = time
        elif intersections < intersect_factor and is_start:
            is_start = False
            intersect_time += time - current_start

    if is_start:
        intersect_time += 1440 - current_start
    
    return intersect_time


data = sys.stdin.read().split()
n = int(data[0])

time_intervals = []
intersect_factor = n
for i in range(1, len(data), 4):
    start = int(data[i]) * 60 + int(data[i + 1])
    end = int(data[i + 2]) * 60 + int(data[i + 3])
    if start == end:
        time_intervals.append([0, 1440])
    elif start > end:
        time_intervals.append([start, 1440])
        time_intervals.append([0, end])
    else:
        time_intervals.append([start, end])

print(get_intersect_time(time_intervals, intersect_factor))
