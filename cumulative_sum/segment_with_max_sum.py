# https://informatics.msk.ru/mod/statements/view.php?id=67323&chapterid=1584#1

def get_segment_with_max_sum(array):
    
    n = len(array)
    
    max_sum = -float('inf')
    max_sum_l = -1
    max_sum_r = -1
    
    min_sum = 0
    min_sum_idx = -1
    
    cumsum = 0
    
    for i in range(n):
        cumsum += array[i]
        
        if cumsum - min_sum > max_sum:
            max_sum = cumsum - min_sum 
            max_sum_r = i
            max_sum_l = min_sum_idx + 1
        
        if cumsum <= min_sum:
            min_sum = cumsum
            min_sum_idx = i
            
    return max_sum_l + 1, max_sum_r + 1
        


n = int(input())
array = [int(input()) for _ in range(n)]
    
print('\n'.join(map(str, get_segment_with_max_sum(array))))
