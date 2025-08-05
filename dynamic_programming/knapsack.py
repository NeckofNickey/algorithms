# https://stepik.org/lesson/1489019/step/3?unit=1508913
# Задача о рюкзаке

def knapsack(weights, values, W):
    
    n = len(weights)
    
    matrix = [[0] * (W + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(W + 1):
            if weights[i - 1] <= j:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                matrix[i][j] = matrix[i - 1][j]   

    return matrix[n][W]


# Пример использования
weights = [1, 2, 3]
values = [10, 15, 40]
W = 5  # Вместимость рюкзака

result = knapsack(weights, values, W)
print(f"Максимальная ценность: {result}")