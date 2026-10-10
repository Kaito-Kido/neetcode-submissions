# Is empty a subet of nums?
# Are any constrants on the length of nums?
# Is the given nums sorted?
# Does 2, 3 and 3, 2 count by 1 subset?
# Can the given nums be empty?

# Approach
# Backtracking + recursive
# At each recursive step, use a for loop to pick a number from left to right
# the next recursive only can pick a number from the next number to the end.
# After pick to the end of the array. add the result to the array result.
# Get back from resursion, and pick the next number next to it.
# Time complexity: O(n^n)
# Space complexity: O(n) stack call
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def recur(index, result, currentResult):
            result.append(currentResult.copy())
            for i in range(index, len(nums)):
                currentResult.append(nums[i])
                recur(i + 1, result, currentResult)
                currentResult.pop()
        
        recur(0, result, [])
        return result
