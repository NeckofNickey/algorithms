# https://informatics.msk.ru/mod/statements/view.php?id=67323&chapterid=2771#1

def get_sum_on_segment(x, y, array):
    
    if not array:
        return 0
    
    n = len(array)
    
    if y > n:
        return 0
     
    cumsum_list = [0]
    
    last = 0
    
    for i in range(n):
        last += array[i]
        cumsum_list.append(last)
        
    
    return cumsum_list[y] - cumsum_list[x - 1]


a, r = tuple(map(int, input().split()))
array = list(map(int, input().split()))

for _ in range(r):
    x, y = tuple(map(int, input().split()))
    print(get_sum_on_segment(x, y, array)) 