# https://informatics.msk.ru/mod/book/view.php?id=488&forceview=1
# https://informatics.msk.ru/mod/statements/view.php?id=766&chapterid=1792#1

def get_lis(seq):
    
    n = len(seq)
    
    # Инициализация: длина LIS для каждого элемента как минимум 1
    length = [1] * n
    predecessor = [-1] * n # -1 означает отсутствие предшественника
    
    # Заполняем массивы длины и предшественника
    for i in range(n):
         for j in range(i + 1, n):
            if seq[j] > seq[i] and length[i] + 1 > length[j]:
                length[j] = length[i] + 1
                predecessor[j] = i # предшественник a[j] в цепочке
                
    # Находим индекс элемента с максимальной длиной LIS
    max_len = max(length)
    current_index = length.index(max_len)

    # Восстанавливаем подпоследовательность
    lis = []
    while current_index != -1:
        lis.append(seq[current_index])
        current_index = predecessor[current_index]
    
            
    return lis[::-1]  # Разворачиваем, так как добавляли с конца

n = int(input())
seq = list(map(int, input().split()))
lis = get_lis(seq)
print(' '.join(map(str, lis)))