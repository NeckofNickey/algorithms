# https://informatics.msk.ru/mod/statements/view.php?id=77938&chapterid=126#1
# Установить значение бита в 0


def get_num(num, bit):
    
    return num & ~(1 << bit)


num, bit = tuple(map(int, input().split()))
print(get_num(num, bit))