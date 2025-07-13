# https://informatics.msk.ru/mod/statements/view.php?id=1966&chapterid=1#1
# Коровы - в стойла

import sys

def get_max_min_distance(n, k, stalls):
    
    stalls.sort()
    
    left = 1
    right = stalls[-1] - stalls[0]
    answer = 0
    
    def can_place_cows(min_dist):
        count = 1
        last_pos = stalls[0]
        for pos in stalls[1:]:
            if pos - last_pos >= min_dist:
                count += 1
                last_pos = pos
                if count > k:
                    return True
        
        return count >= k
    
    while left <= right:
        mid = (left + right) // 2
        if can_place_cows(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return answer


data = sys.stdin.read().split()
n = int(data[0])
k = int(data[1])

stalls = list(map(int, data[2:2 + n]))

max_min_distance = get_max_min_distance(n, k, stalls)

sys.stdout.write(str(max_min_distance))