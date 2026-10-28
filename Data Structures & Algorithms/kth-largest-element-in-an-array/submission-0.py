class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                minval = heap[0]
                if num > minval:
                    heapq.heappush(heap, num)
                    heapq.heappop(heap)
        
        return heap[0]