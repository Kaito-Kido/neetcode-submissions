class Solution:
    # Intuition:
    # If we precompute the max of left and right land at each point we could calculate the height of water at that point
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n

        currentMax = 0
        for i in range(n):
            if i == 0:
                currentMax = max(height[i], currentMax)
                continue
            
            leftMax[i] = currentMax
            currentMax = max(height[i], currentMax)
        
        currentMax = 0
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                currentMax = max(height[i], currentMax)
                continue
            rightMax[i] = currentMax
            currentMax = max(height[i], currentMax)

        area = 0
        for index, h in enumerate(height):
            area += max(min(leftMax[index], rightMax[index]) - h, 0)
        
        return area


            