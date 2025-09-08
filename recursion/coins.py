# https://informatics.msk.ru/mod/statements/view.php?id=77802&chapterid=157#1
# Монетки

import sys

def main():

    data = sys.stdin.read().split()
    if not data:
        print(-1)
        return
        
    it = iter(data)
    N = int(next(it))
    M = int(next(it))
    coins = [int(next(it)) for _ in range(M)]
    
    total_sum = 2 * sum(coins)
    if total_sum < N:
        print(-1)
        return
        
    # Теперь ищем комбинацию
    best_count = float('inf')
    best_combination = None
    
    # Рекурсивная функция перебора
    def backtrack(idx, current_sum, count, used):
        nonlocal best_count, best_combination
        if current_sum > N:
            return
        if idx == M:
            if current_sum == N:
                if count < best_count:
                    best_count = count
                    best_combination = used[:]
            return
        
        # Варианты: взять 0, 1 или 2 монеты текущего номинала
        for take in range(0, 3):
            new_sum = current_sum + take * coins[idx]
            new_count = count + take
            # Отсечение по количеству монет
            if new_count > best_count:
                continue
            used.append(take)
            backtrack(idx+1, new_sum, new_count, used)
            used.pop()
    
    backtrack(0, 0, 0, [])
    
    if best_combination is None:
        print(0)
    else:
        # Восстанавливаем список монет
        result_coins = []
        for i in range(M):
            for j in range(best_combination[i]):
                result_coins.append(coins[i])
        # Сортируем по убыванию? (по условию вывод любой)
        # Но в примере вывод: 40,30,30
        print(best_count)
        print(" ".join(map(str, result_coins)))

if __name__ == "__main__":
    main()