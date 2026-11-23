# Constraint:
# 1 <= nums.length <= 100
# so if nums.length == 1 return false because we can't split it into 2 subset
# if the sum of they array is odd, we can't split it into 2 equal subset
# So we just need to compare the current subset sum with half a sum of the array.
# -> turn to n sum problem -> select coin problem

# Bruteforce
# At each step we can choose to pick or not pick the element
# After finishing compare it with the remaining sum of the other subset
# pruning using sum of the array.
# Time complexity is O(2^n)
# Space complexity is O(1)

# Invariant
# So we have the sum and we gonna sort the array
# using dp we have dp[remainSum][i] where i is the current index
# dp[remainSum, i] = (dp[remainSum - nums[i], i + 1] OR dp[remainSum, i + 1]) - transition function
# base case remainSum == nums[i]
# Time complexity O(remainSum * n)
# Space complexity O(remainSum * n)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False

        remainSum = 0
        for num in nums:
            remainSum += num
        
        if remainSum % 2 != 0:
            return False
        
        remainSum = remainSum // 2

        dp = [[None for _ in range(len(nums) + 1)] for i in range(remainSum + 1)]

        def recurse(remainSum, index):
            if dp[remainSum][index] != None:
                return dp[remainSum][index]

            if index == len(nums):
                return False
            if remainSum == 0:
                return True
            if remainSum == nums[index]:
                return True
       
            first = False
            if index + 1 < len(nums) and dp[remainSum][index+1] == None:
                dp[remainSum][index+1] = recurse(remainSum, index + 1)
                first = dp[remainSum][index+1]
            
            second = False
            if remainSum >= nums[index] and dp[remainSum - nums[index]][index + 1] == None:
                dp[remainSum - nums[index]][index+1] = recurse(remainSum - nums[index], index + 1)
                second = dp[remainSum - nums[index]][index+1]
            
            dp[remainSum][index] = first or second
            return dp[remainSum][index]
        
        return recurse(remainSum, 0)





