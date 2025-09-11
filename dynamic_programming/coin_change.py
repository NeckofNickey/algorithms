# https://leetcode.com/problems/coin-change/description/
# 322. Coin Change

def coinChange(coins, amount: int) -> int:
    
    dp = [0] * (amount + 1)
    
    for i in range(1, amount + 1):
        
        min_coins = float('inf')
        
        for coin in coins:
            if coin <= i:
                min_coins = min(min_coins, dp[i - coin] + 1)
        
        dp[i] = min_coins

    return dp[-1] if dp[-1] != float('inf') else -1

coins = eval(input())
amount = int(input())
print(coinChange(coins, amount))