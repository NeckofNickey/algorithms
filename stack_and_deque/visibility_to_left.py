# https://new.contest.yandex.ru/contests/80787/problems?id=149944%2F2025_08_30%2FInC5MNC6Cd
# Видимость влево

n = int(input())

arr = list(map(int, input().split()))

stack = []

result = [0] * n

for i in range(n):
    
    while stack and arr[i] > stack[-1][0]:
        num, idx = stack.pop()
        result[i] += result[idx] + 1

    stack.append((arr[i], i))


    
    
print(' '.join(map(str, result)))