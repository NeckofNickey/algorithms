# https://leetcode.com/problems/top-k-frequent-elements/description/
# 347. Top K Frequent Elements

import heapq
from collections import Counter


def topKFrequent(nums, k):
    freq = Counter(nums)

    heap = [(-count, num) for num, count in freq.items()]
    heapq.heapify(heap)

    return [heapq.heappop(heap)[1] for _ in range(k)]


nums = eval(input())
k = int(input())
print(topKFrequent(nums, k))