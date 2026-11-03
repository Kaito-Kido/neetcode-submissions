

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(currentIndex, remain, currentResult, previous, pick):
            if remain == 0:
                result.append(currentResult.copy())
            if currentIndex >= len(candidates):
                return -1
                
            candidate = candidates[currentIndex]
            if candidate > remain:
                return -1

            backtrack(currentIndex + 1, remain, currentResult, candidate, False)
            if previous != candidate or pick:
                currentResult.append(candidate)
                backtrack(currentIndex + 1, remain - candidate, currentResult, candidate, True)
                currentResult.pop()

        candidates.sort()
        backtrack(0, target, [], -1, True)
        return result