# https://informatics.msk.ru/mod/statements/view.php?id=67323&chapterid=2771#1

# превышено максимальное время раб

def get_cumsum_list(array):
    
    n = len(array)
    
    cumsum_list = [0] * (n + 1)

    for i in range(n):
        cumsum_list[i + 1] = cumsum_list[i] + array[i]

    return cumsum_list


a, r = tuple(map(int, input().split()))
array = list(map(int, input().split()))

cumsum_list = get_cumsum_list(array)

for _ in range(r):
    x, y = tuple(map(int, input().split()))
    print(cumsum_list[y] - cumsum_list[x - 1])