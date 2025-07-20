# https://informatics.msk.ru/mod/statements/view.php?id=77938&chapterid=128#1
# Определить значение бита

def get_bit(num, bit):
    
    return (num >> bit) & 1 


num, bit = tuple(map(int, input().split()))
print(get_bit(num, bit))