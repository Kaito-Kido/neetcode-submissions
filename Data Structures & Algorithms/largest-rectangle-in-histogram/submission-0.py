class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque()
        n = len(heights)
        leftMost = [-1] * n
        rightMost = [n] * n

        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)

        area = 0
        for i in range(n):
            left = leftMost[i] + 1
            right = rightMost[i] - 1
            area = max(area, (right - left + 1) * heights[i])
        return area


