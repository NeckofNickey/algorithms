# https://informatics.msk.ru/mod/statements/view.php?id=77938&chapterid=123#1
# 2^n

def get_num(degree):
    
    return 1 << degree

degree = int(input())
print(get_num(degree))