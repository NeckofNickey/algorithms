# https://informatics.msk.ru/mod/statements/view.php?id=77938&chapterid=122#1
# 2^n+2^m

def get_num(n, m):
    
    return 1 << n | 1 << m


n, m = tuple(map(int, input().split()))
print(get_num(n, m))