class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inserted = False

        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                intervals.insert(i, newInterval)
                inserted = True
                break

        if not inserted:
            intervals.append(newInterval)

        output = []

        for interval in intervals:
            if not output:
                output.append(interval)
                continue

            if interval[0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], interval[1])
            else:
                output.append(interval)

        return output