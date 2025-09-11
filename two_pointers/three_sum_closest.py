# https://leetcode.com/problems/3sum-closest/description/
# 16. 3Sum Closest


def threeSumClosest(nums, target: int) -> int:
    
    n = len(nums)
    
    nums.sort()
    
    closest_sum = float('inf')
    
    for i in range(n):
        
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, n - 1
        
        while left < right:
            
            total = nums[left] + nums[right] + nums[i]
            
            if abs(total - target) <= abs(closest_sum - target):
                closest_sum = total
            
            if total - target == 0:
                return total
            elif total - target > 0:
                right -= 1
            else:
                left += 1
            
    return closest_sum


nums = eval(input())
target = int(input())

print(threeSumClosest(nums, target))