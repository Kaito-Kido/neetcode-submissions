"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


# Clarification
# did the array sorted by startTime? no
# can the given intervals be empty? if so what should i return: maybe true
# My Approach:
# Sort intervals by start time and check pair interval if currentInterval[0] > prevInterval[1] curent mêeting start time <previous meeting end time)
# Time complexity is O(nlogn)
# space complexity O(n)
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x: x.start)
        for index, interval in enumerate(intervals):
            if index == 0:
                continue
            
            if interval.start < intervals[index - 1].end:
                return False
        
        return True