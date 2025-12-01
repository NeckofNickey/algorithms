# https://leetcode.com/problems/subarray-sum-equals-k/description/
# 560. Subarray Sum Equals K

def subarraySum(nums, k):
    
    count = 0
    prefix_sum = 0
    prefix_map = {0: 1}  # сумма 0 встречается 1 раз (пустой подмассив)
    
    for num in nums:
        prefix_sum += num
        
        # Если (prefix_sum - k) существует в мапе, значит есть подмассив с суммой k
        if (prefix_sum - k) in prefix_map:
            count += prefix_map[prefix_sum - k]
        
        # Обновляем количество встреч текущей префиксной суммы
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
    
    return count


nums = eval(input())
k = int(input())
print(subarraySum(nums, k))