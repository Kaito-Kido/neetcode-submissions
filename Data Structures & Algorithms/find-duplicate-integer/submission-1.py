class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        index1 = 0
        index2 = 0

        while 1:
            index1 = nums[index1]
            index2 = nums[nums[index2]]
        
            if index1 == index2:
                break
        
        index1 = 0
        while index1 != index2:
            index1 = nums[index1]
            index2 = nums[index2]
        
        return index1
