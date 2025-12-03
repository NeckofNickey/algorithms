# https://informatics.msk.ru/mod/statements/view.php?chapterid=2998#1
# Плавные числа

def get_amount_of_smooth_num(lenghth):
    
    dp = [1] * 12
    dp[0] = dp[1] = dp[-1] = 0

    for _ in range(lenghth - 1):
        temp_dp = [x for x in dp]
        for i in range(1, len(dp) - 1):
            temp_dp[i] = dp[i - 1] + dp[i] + dp[i + 1]
        
        dp = temp_dp

    return sum(dp)



lenghth = int(input())
print(get_amount_of_smooth_num(lenghth))