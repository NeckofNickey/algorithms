# https://informatics.msk.ru/mod/statements/view.php?id=1966&chapterid=414#1
# Эльфы и олени

# Решается не корректно

import sys

def get_solve(m, n, a_list, b_list):
    
    # Сортируем с сохранением исходных индексов (нумерация с 1)
    deer = sorted([(a_list[i], i + 1) for i in range(m)], key=lambda x: x[0])
    elves = sorted([(b_list[i], i + 1) for i in range(n)], key=lambda x: x[0])
    
    low = 0
    high = min(m, n // 2)
    best_k = 0
    
    def is_possible(K):
        if K == 0:
            return True, []
        
        # Первые K эльфов (наименьшие b_i)
        first_K = elves[:K]
        # Последние K эльфов (наибольшие b_i)
        last_K = elves[-K:]
        
        pairs = []
        deer_ptr = 0
        first_ptr = 0
        last_ptr = 0
        
        while deer_ptr < K and first_ptr < K and last_ptr < K:
            current_deer = deer[deer_ptr]
            current_first = first_K[first_ptr]
            current_last = last_K[last_ptr]
            
            if current_first[0] < current_deer[0] < current_last[0]:
                pairs.append((current_deer[1], current_first[1], current_last[1]))
                deer_ptr += 1
                first_ptr += 1
                last_ptr += 1
            elif current_deer[0] <= current_first[0]:
                # Пропускаем этого оленя, он слишком "маленький"
                deer_ptr += 1
            else:
                # Пропускаем этого эльфа, он слишком "большой"
                last_ptr += 1
        
        if len(pairs) >= K:
            return True, pairs[:K]
        else:
            return False, []
    
    # Бинарный поиск по K
    while low <= high:
        mid = (low + high) // 2
        possible, _ = is_possible(mid)
        if possible:
            best_k = mid
            low = mid + 1
        else:
            high = mid - 1
    
    # Получаем финальные пары для best_k
    possible, pairs = is_possible(best_k)
    
    return pairs
    
    


data = sys.stdin.read().split()
m = int(data[0])
n = int(data[1])
a_list = list(map(int, data[2:2 + m]))
b_list = list(map(int, data[2 + m:2 + m + n]))


result = get_solve(m, n, a_list, b_list)
print(len(result))
for res in result:
    print(' '.join(map(str, res)))
