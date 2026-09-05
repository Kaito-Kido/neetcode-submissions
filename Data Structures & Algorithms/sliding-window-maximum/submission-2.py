# Initial approach:
# Maintain a heap with k capacity
# Time complexity: O(nlogk)
# Space complexity: O(k)


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # save index
        result = []
        for i, num in enumerate(nums):
            while q and q[0] <= i - k:
                q.popleft()
            

            while q and nums[q[-1]] <= num:
                q.pop()
            
            q.append(i)
            
            if i >= k - 1:
                result.append(nums[q[0]])

        return result


