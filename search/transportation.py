# https://informatics.msk.ru/mod/statements/view.php?id=193&chapterid=1967#1
# Транспортировка

import sys
import heapq


def can_deliver(n, edges, max_time, total_weight):
    graph = [[] for _ in range(n + 1)]
    for u, v, time, limit in edges:
        if limit >= total_weight:
            graph[u].append((v, time))
            graph[v].append((u, time))

    time_list = [float('inf')] * (n + 1)
    time_list[1] = 0
    pq = [(0, 1)]

    while pq:
        t, u = heapq.heappop(pq)
        if t > time_list[u]:
            continue
        if u == n:
            return t <= max_time
        for v, time in graph[u]:
            nt = t + time
            if nt < time_list[v]:
                time_list[v] = nt
                heapq.heappush(pq, (nt, v))

    return False


data = list(map(int, sys.stdin.read().split()))
idx = 0
n = data[idx]; idx += 1
m = data[idx]; idx += 1

edges = []

for i in range(idx, len(data), 4):
    u, v, t, w = data[i], data[i + 1], data[i + 2], data[i + 3]
    edges.append((u, v, t, w))

TRACK_WEIGHT = 3000000
CUP_WEIGHT = 100

left, right = 0, 10**7

max_cup = 0

while left <= right:
    mid = (left + right) // 2
    total_weight = TRACK_WEIGHT + CUP_WEIGHT * mid
    if can_deliver(n, edges, 1440, total_weight):
        max_cup = mid
        left = mid + 1
    else:
        right = mid - 1

print(max_cup)