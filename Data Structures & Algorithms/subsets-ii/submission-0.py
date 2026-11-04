# Requirements and Contraints
# Solution must not contain duplicate subsets.
# [] is a subset
# 1 <= nums.length <= 11
# -20 <= nums[i] <= 20

# Backtracking approach
# Sort the array to easyly skip duplicate subset, and because the returned solution can be in any order
# at each cursive, interate through nums to pick a num.
# not pick should be pick first because the result is the assembly of [] * nums.length
# consecutive values should be skipped to remove duplicate subsets

# Time complexity: O(n * 2^n)
# Space complexity: O(n) which is n is recursive stack
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        path = []
        start = 0
        def backtracking(start):
            result.append(path.copy())

            for i in range(start, len(nums)): # handle the last element before reach the terminal condition
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtracking(i + 1)
                path.pop()
            
        backtracking(0)

        return result


