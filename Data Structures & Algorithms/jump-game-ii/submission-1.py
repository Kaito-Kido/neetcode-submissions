
# Time complexity: O()
class Solution:
    def jump(self, nums: List[int]) -> int:
        minimumjump = [-1 for i in range(len(nums))]
        minimumjump[0] = 0

        for i in range(len(nums)):
            for j in range(i + 1, min(i + nums[i] + 1, len(nums))):
                if minimumjump[j] == -1:
                    minimumjump[j] = minimumjump[i] + 1
                else:
                    minimumjump[j] = min(minimumjump[j], minimumjump[i] + 1)
        return minimumjump[-1]


