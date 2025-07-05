# https://informatics.msk.ru/mod/statements/view.php?id=67323&chapterid=1584#1

def get_segment_with_max_sum(array):
    
    n = len(array)
    
    current_max = array[0]
    global_max = array[0]
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(1, n):
        if array[i] > current_max + array[i]:
            current_max = array[i]
            temp_start = i
        else:
            current_max += array[i]
    
        # Обновляем global_max и индексы, если текущая сумма больше
        # или если суммы равны, но j меньше или i больше
        if (current_max > global_max) or \
        ((current_max == global_max) and (i < end or (i == end and temp_start >= start))):
            global_max = current_max
            start = temp_start
            end = i   
    
    return ([start + 1, end + 1])
        


n = int(input())
array = [int(input()) for _ in range(n)]
    
print('\n'.join(map(str, get_segment_with_max_sum(array))))
