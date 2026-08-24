class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])

        result = []

        for inter in intervals:
            if not result:
                result.append(inter)
                continue
            
            if inter[0] < result[-1][1]:
                result[-1][1] = min(result[-1][1], inter[1])
            else:
                result.append(inter)
        
        return len(intervals) - len(result)