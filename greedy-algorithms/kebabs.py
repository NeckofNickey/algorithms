def get_max_num_of_servings(param_list):
    
    k, a, b, x, y = param_list
    max_servings = 0
    
    # Максимальное количество порций первого блюда, если готовить только его
    max_n = 0
    if k >= a:
        max_n = (k - a) // x + 1
        
    # Максимальное количество порций второго блюда, если готовить только его
    max_m = 0
    if k >= b:
        max_m = (k - b) // y + 1
        
        
    # Перебираем возможные n от 0 до min(max_n, k // x)
    # и для каждого вычисляем m = (k - n * x) // y
    # Ограничиваем перебор разумными пределами, например, 2e5
    limit = min(max_n, 2*10**5)
    for n in range(limit + 1):
        remaining = k - n * x
        if remaining < 0:
            break
        m = 0
        if remaining >= b:
            m = (remaining - b) // y + 1
        max_servings = max(max_servings, n + m)
        
    
    limit = min(max_m, 2*10**5)    
    for m in range(limit + 1):
        remaining = k - m * y
        if remaining < 0:
            break
        n = 0
        if remaining >= a:
            n = (remaining - a) // x + 1
        max_servings = max(max_servings, n + m)
    
    return max_servings
            
        
n = int(input())
result_list = []

for _ in range(n):
    param_list = list(map(int, input().split()))
    result_list.append(get_max_num_of_servings(param_list))
    
for num in result_list: 
    print(num)