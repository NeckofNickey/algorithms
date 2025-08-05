# https://stepik.org/lesson/1489019/step/1?unit=1508913
# Размен монет

import sys

def coin_change(coins_list, amount):
    
        coins_list.sort(reverse=True)
        coin_counter = 0
        
        for coin in coins_list:
            
            while amount >= coin:
                amount -= coin
                coin_counter += 1
            
        return coin_counter if amount == 0 else -1



data = list(map(int, sys.stdin.read().split()))
index = 0
n = data[0]
index += 1
coins_list = data[index: index + n]
index += n
amount = data[index]

sys.stdout.write(str(coin_change(coins_list, amount)))

