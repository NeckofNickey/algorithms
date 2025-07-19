# https://informatics.msk.ru/mod/statements/view.php?id=77938&chapterid=121#1
# Обнулить последние биты

def get_num(num, n):
    mask = (-1) << n
    return num & mask

num, n = map(int, input().split())
print(get_num(num, n))