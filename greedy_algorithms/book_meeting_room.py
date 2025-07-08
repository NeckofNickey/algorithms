# https://new.contest.yandex.ru/contests/48557/problem?id=215%2F2023_04_06%2FRdGbbmsLQn

# def book_meeting_room(intervals):
    
#     if not intervals:
#         return 0
    
#     suitable_intervals = []

#     while intervals:

#         min_right = float('inf')

#         for interval in intervals:
#             if interval[1] < min_right:
#                 min_right = interval[1]

#         for interval in intervals:
#             if interval[1] == min_right:
#                 suitable_intervals.append(interval)
#                 intervals.remove(interval)
#                 break
        
#         intervals_copy = [i for i in intervals]
        
#         for interval in intervals_copy:
#             if suitable_intervals[-1][0] <= interval[1] and suitable_intervals[-1][1] >= interval[0]:
#                 intervals.remove(interval)
                
#     return len(suitable_intervals)


def book_meeting_room(intervals):
    if not intervals:
        return 0
    
    # Сортируем интервалы по правой границе
    intervals.sort(key=lambda x: x[1])
    
    suitable_intervals = [intervals[0]]
    
    for interval in intervals[1:]:
        # Если текущий интервал не пересекается с последним выбранным
        if interval[0] > suitable_intervals[-1][1]:
            suitable_intervals.append(interval)
    
    return len(suitable_intervals)


n = int(input())
intervals = []

for _ in range(n):
    intervals.append([int(x) for x in input().strip().split()])

print(book_meeting_room(intervals))