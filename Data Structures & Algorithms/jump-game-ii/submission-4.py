
# Time complexity: O()
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        currentEnd = 0
        farthest = nums[0] + 1
        count = 0

        while farthest < len(nums): 
            newPos = -1
            for i in range(currentEnd, farthest):
                newPos = max(nums[i] + i, newPos)
            
            count += 1
            currentEnd = farthest
            farthest = newPos + 1

        return count + 1


