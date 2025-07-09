# https://informatics.msk.ru/mod/statements/view.php?id=3516&chapterid=3570#1
# Деление пополам (поиск корня n-ой степени методом бинарного поиска)


def get_root(n, num):
    
    if num == 1 or num == 0:
        return num
    
    start_num = 0
    end_num = max(1, num)
    
    root = -1
    
    while abs(root ** n - num) > 0.000001:
        mid_num = (start_num + end_num) / 2
        
        if mid_num**n == num:
            return mid_num
        elif mid_num**n > num:
            root = mid_num
            end_num = mid_num
        else:
            root = mid_num
            start_num = mid_num
            
    return root
        

num = float(input())
n = int(input())

print(get_root(n, num))
