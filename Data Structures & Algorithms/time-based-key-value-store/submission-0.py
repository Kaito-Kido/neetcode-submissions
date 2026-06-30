class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        left, right = 0, len(self.map[key]) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_time = self.map[key][mid][1]

            if mid_time == timestamp:
                return self.map[key][mid][0]
            elif mid_time < timestamp:
                left = mid + 1
            else:
                right = mid - 1

        if right < 0:
            return ""

        return self.map[key][right][0]
