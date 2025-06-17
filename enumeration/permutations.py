# https://new.contest.yandex.ru/contests/48556/problem?id=215%2F2023_04_06%2FxAmHQ1PYv2

def get_num_of_perm(num):

    if num in (0, 1):
        return 1

    num_of_perm = 1

    for i in range(2, num + 1):
        num_of_perm *= i

    return num_of_perm

num = int(input())

print(get_num_of_perm(num))