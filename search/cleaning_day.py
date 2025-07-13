# https://informatics.msk.ru/mod/statements/view.php?id=1966&chapterid=1620#1
# Субботник

import sys

def get_min_max_inconvenience(n, r, c, heights_list):
    
    heights_list.sort()

    left = 0
    right = heights_list[-1] - heights_list[0]
    answer = right
    
    def is_possible(max_diff):
        brigades = 0
        i = 0
        
        while i <= n - c:
            if heights_list[i + c - 1] - heights_list[i] <= max_diff:
                brigades += 1
                i += c
            else:
                i += 1
            if brigades >= r:
                return True
        
        return brigades >= r
    
    
    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1    
            
    return answer
    

data = sys.stdin.read().split()

n = int(data[0])
r = int(data[1])
c = int(data[2])

heights_list = list(map(int, data[3:3 + n]))

min_max_inconvenience = get_min_max_inconvenience(n, r, c, heights_list)

sys.stdout.write(str(min_max_inconvenience))




