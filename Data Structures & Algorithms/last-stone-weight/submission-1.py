class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) >= 2:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)

            if first == second:
                continue
            
            heapq.heappush(heap, -abs(first - second))
        
        if len(heap) == 0:
            return 0
        else:
            return abs(heapq.heappop(heap))

