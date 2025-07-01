# https://codeforces.com/problemset/problem/2113/A

def get_max_num_of_servings(param_list):
    
    k, a, b, x, y = param_list
    max_servings = 0
    
    if y < x:
        a, b, x, y = b, a, y, x
    
    # Максимальное количество порций первого блюда, если готовить только его
    max_n = 0
    if k >= a:
        max_n = (k - a) // x + 1
        
    remaining_heat = k - max_n * x
        
    # Максимальное количество порций второго блюда, если готовить только его
    max_m = 0
    if remaining_heat >= b:
        max_m = (remaining_heat - b) // y + 1
        
    return max_n + max_m
            
        
n = int(input())
result_list = []

for _ in range(n):
    param_list = list(map(int, input().split()))
    result_list.append(get_max_num_of_servings(param_list))
    
for num in result_list: 
    print(num)