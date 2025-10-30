# https://leetcode.com/problems/count-primes/description/
# 204. Count Primes

# Алгоритм "Решето Эратосфена"

def countPrimes(n: int) -> int:
        
    if n < 2:
            return 0

    mask = [True] * (n)
    mask[0] = False
    mask[1] = False

    for i in range(2, int(n**0.5) + 1):
        if mask[i]:
            for j in range(i * i, n, i):
                mask[j] = False
    
    return sum(mask)


n = int(input())
print(countPrimes(n))