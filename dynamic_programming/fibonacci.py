# https://stepik.org/lesson/1489019/step/3?unit=1508913
# Числа Фибоначчи

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    
    return memo[n]


print(fibonacci(10))