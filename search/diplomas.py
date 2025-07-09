# https://informatics.msk.ru/mod/statements/view.php?id=1966&chapterid=1923#1
# Дипломы

def get_min_square_for_diplomas(w, h, n):
    
    left = 0
    right = max(w, h) * n
    
    while left < right:
        mid = (left + right) // 2
        if (mid // h) * (mid // w) >= n:
            right = mid
        else:
            left = mid + 1
            
    return left 


w, h, n = map(int, input().split())
print(get_min_square_for_diplomas(w, h, n))