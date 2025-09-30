# https://informatics.msk.ru/mod/statements/view.php?id=76680#1
# Велогонка
import sys

def get_min_dist(n, cyclists):
    
    # Функция расстояния между лидером и замыкающим в момент t
    def dist(t):
        positions = [x + v * t for x, v in cyclists]
        return max(positions) - min(positions)
    
    # Тернарный поиск по t
    left, right = 0.0, 1e7
    for _ in range(100):  # 100 итераций для точности ~1e-30
        t1 = left + (right - left) / 3
        t2 = right - (right - left) / 3
        d1 = dist(t1)
        d2 = dist(t2)
        if d1 < d2:
            right = t2
        else:
            left = t1
    
    t_ans = (left + right) / 2
    l_ans = dist(t_ans)
    
    return f"{t_ans:.10f} {l_ans:.10f}"

data = sys.stdin.read().split()
    
n = int(data[0])

cyclists = []
idx = 1
for i in range(n):
    x = int(data[idx])
    v = int(data[idx + 1])
    idx += 2
    cyclists.append((x, v))


print(get_min_dist(n, cyclists))
