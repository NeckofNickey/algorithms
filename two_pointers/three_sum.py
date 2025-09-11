# https://leetcode.com/problems/3sum/description/
# 3Sum

def threeSum(nums):
    
    n = len(nums)
    
    nums.sort()
    
    result = []
    
    for i in range(n):
        
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, n - 1
        
        while left < right:
            if nums[left] + nums[right] == -nums[i]:
                result.append([nums[left], nums[right], nums[i]])
                left += 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            elif nums[left] + nums[right] > -nums[i]:
                right -= 1
            else:
                left += 1
    
    return result



nums = eval(input())
print(threeSum(nums))