class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        result = []
        currentResult = []
        def backtrack():
            if len(currentResult) == len(nums):
                result.append(currentResult.copy())
                return
            for num in nums:
                if num in visited:
                    continue

                visited.add(num)
                currentResult.append(num)
                backtrack()
                visited.remove(num)
                currentResult.pop()
        backtrack()
        return result