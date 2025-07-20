# https://informatics.msk.ru/mod/statements/view.php?id=77938&chapterid=127#1
# Обнулить все биты, кроме последних

def get_num(num, n):
    mask = (1 << n) - 1
    return num & mask

num, n = map(int, input().split())
print(get_num(num, n))