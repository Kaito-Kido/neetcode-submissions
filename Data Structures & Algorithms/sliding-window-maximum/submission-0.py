# Initial approach:
# Maintain a heap with k capacity
# Time complexity: O(nlogk)
# Space complexity: O(k)


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxheap = []
        result = []

        for i in range(k):
            heapq.heappush(maxheap, (-nums[i], i))
        result.append(-maxheap[0][0])
        
        resultindex = k

        while resultindex < len(nums):
            heapq.heappush(maxheap, (-nums[resultindex], resultindex))

            while maxheap and maxheap[0][1] <= resultindex - k:
                heapq.heappop(maxheap)
            
            result.append(-maxheap[0][0])
            resultindex += 1
        
        return result
            


