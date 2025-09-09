# https://leetcode.com/problems/delete-and-earn/description/
# Delete and Earn


def rob(nums) -> int:
    
    from collections import defaultdict
    points = defaultdict(int)
    max_num = 0
    
    for num in nums:
        points[num] += num
        max_num = max(max_num, num)
    
    dp = [0] * (max_num + 1)
    dp[1] = points.get(1, 0)
    
    for num in range(2, max_num + 1):
        dp[num] = max(dp[num - 1], dp[num - 2] + points.get(num, 0))
    
    return dp[max_num]
    


money_list = list(map(int, input().split()))
print(rob(money_list))