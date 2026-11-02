"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key=lambda x: x.start)
        heap = []
        maxoverlap = 0

        for interval in intervals:
            while heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            
            heapq.heappush(heap, interval.end)
            maxoverlap = max(maxoverlap, len(heap))
        
        return maxoverlap