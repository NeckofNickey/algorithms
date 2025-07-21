# https://informatics.msk.ru/mod/statements/view.php?id=77938&chapterid=1007#1
# Забавная игра

def get_max_num(num):
    
    bin_num = bin(num)[2:]
    max_num = num
    
    for i in range(len(bin_num)):
        shifted = bin_num[-i:] + bin_num[:-i]
        current = int(shifted, 2)
        if current > max_num:
            max_num = current
    
    return max_num


num = int(input())
print(get_max_num(num))