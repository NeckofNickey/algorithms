# https://leetcode.com/problems/permutations/description/
# Permutations

def permute(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
              return []

        if len(nums) > 1:
            for i in range 