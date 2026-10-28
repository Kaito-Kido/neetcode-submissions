class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == 0:
            return []
        heap = []

        for point in points:
            distance = point[0]**2 + point[1]**2
            
            if len(heap) < k:
                heapq.heappush(heap, (-distance, point))
            else:
                last = -heap[0][0]
                if distance <= last:
                    heapq.heappush(heap, (-distance, point))
                    if len(heap) > k:
                        heapq.heappop(heap)
        
        result = []
        for h, point in heap:
            result.append(point)
        return result
