class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        result = [0] * len(temperatures)
        for index, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                peakIndex = stack[-1][0]
                result[peakIndex] = index - peakIndex
                stack.pop()
            stack.append((index, t))
        
        return result