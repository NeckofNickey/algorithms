# https://new.contest.yandex.ru/contests/48556/problem?id=215%2F2023_04_06%2FyrA534pVxW

def get_num_of_combination(n, k):

    if k > n:
        return 0

    if k == n or k == 0:
        return 1
    
    k = min(k, n - k)

    nominator = 1
    denominator = 1

    for i in range(1, k + 1):
        nominator *= (n - k + i)
        denominator *= i

    return nominator // denominator


n, k = [int(i) for i in input().strip().split()]
print(get_num_of_combination(n, k))