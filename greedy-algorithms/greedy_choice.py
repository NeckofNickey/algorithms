# https://codeforces.com/problemset/problem/10/E?locale=ru

def get_min_coins(coins_list):
    
    max_range = coins_list[0] + coins_list[1] # предел
    
    dp = [float('inf')] * (max_range + 1)
    dp[0] = 0
    
    # Оптимальное решение: DP
    for i in range(1, max_range + 1):
        for coin in coins_list:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Жадное решение и сравнение            
    for i in range(1, max_range + 1):
        greedy_sum = i
        greedy_count = 0
        for coin in coins_list:
            if greedy_sum >= coin:
                greedy_count += greedy_sum // coin
                greedy_sum %= coin
        
        if greedy_count != dp[i]:
            return i
    
    return -1
        
            

n = int(input())
coins_list = list(map(int, input().split()))
print(get_min_coins(coins_list))