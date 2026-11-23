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
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)

        dp = [[False] * (target + 1) for _ in range(n + 1)]

        dp[n][0] = True

        for i in range(n-1, -1, -1):
            for remain in range(target + 1):
                skip = dp[i + 1][remain]
                pick = False
                if remain >= nums[i]:
                    pick = dp[i + 1][remain - nums[i]]

                dp[i][remain] = pick or skip
        
        return dp[0][target]
    







