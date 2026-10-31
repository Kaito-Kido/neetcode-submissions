
# Time complexity: O()
class Solution:
    def jump(self, nums: List[int]) -> int:
        currentEnd = 0
        farthest = 0
        count = 0

        for i in range(len(nums) - 1):
            print(currentEnd, farthest, count)
            farthest = max(farthest, i + nums[i])

            if i == currentEnd:
                count += 1
                currentEnd = farthest
        
        return count



