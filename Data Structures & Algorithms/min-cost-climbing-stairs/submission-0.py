# Brute force:
# Time complexity: O(2^(n-2))
# Space Complexity: O(1)

# Invariant
# for each ith floor we've reached. the previous step can be i-1 or i-2 
# so we just need to get the minimum cost between min(cost[i-1], cost[i-2]) + cost[i]
# cost at first two step is 0
# calculate the current minimum step until reach the n-1 floor
# Time Complexity: O(n)
# Space Complexity: O(1) we only need 2 variables to track the minimum cost at i-1 , i-2
# n is the low boundary because we have to loop through the array to get to know the cost of all floor

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = 0
        second = 0

        for i in range(len(cost)):
            minCost = min(first, second) + cost[i]
            first = second
            second = minCost
        

        return min(first, second)

