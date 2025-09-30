# https://informatics.msk.ru/mod/statements/view.php?id=265&chapterid=196#1
# Степень перестановки

def main():
    import math
    n = int(input())
    perm = list(map(int, input().split()))
    
    visited = [False] * n
    cycles = []
    
    for i in range(n):
        if not visited[i]:
            cycle_len = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = perm[j] - 1  # Переход к следующему элементу
                cycle_len += 1
            if cycle_len > 0:
                cycles.append(cycle_len)
    
    # Находим НОК длин циклов
    lcm = 1
    for length in cycles:
        lcm = lcm * length // math.gcd(lcm, length)
    
    print(lcm)

if __name__ == "__main__":
    main()