class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        intervals.sort(key=lambda x: x[0])
        for interval in intervals:
            if not output:
                output.append(interval)
                continue
            
            if interval[0] <= output[-1][1]:
                if output[-1][1] < interval[1]:
                    output[-1][1] = interval[1]
            else:
                output.append(interval)

        return output
        
