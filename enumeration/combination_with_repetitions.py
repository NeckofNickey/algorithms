# https://new.contest.yandex.ru/contests/48556/problem?id=215%2F2023_04_06%2FWoW7IdbfFr

def get_num_of_combination_with_repetitions(n, k):

    if n == 0:
        return 0

    N = n + k - 1
    K = k

    K = min(K, N - K)

    nominator = 1
    denominator = 1

    for i in range(1, K + 1):
        nominator *= N - K + i
        denominator *= i

    return nominator // denominator


n, k = [int(i) for i in input().strip().split()]
print(get_num_of_combination_with_repetitions(n, k))