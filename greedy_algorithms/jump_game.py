# https://leetcode.com/problems/jump-game/description/
# 55. Jump Game

def canJump(nums) -> bool:
    
    n = len(nums)
    
    max_reach = 0
    
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
        if max_reach >= len(nums) - 1:
            return True
        
    return True
        
nums = eval(input())
print(canJump(nums))