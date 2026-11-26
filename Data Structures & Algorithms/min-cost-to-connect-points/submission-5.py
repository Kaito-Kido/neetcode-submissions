class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        index = 0
        minDist = [float('inf')] * len(points)
        minDist[0] = 0
        while len(visited) < len(points):
            visited.add(index)
            point = points[index]
            for i in range(len(points)):
                if i in visited:
                    continue
                dist = abs(points[i][0] - point[0]) + abs(points[i][1] - point[1])
                minDist[i] = min(minDist[i], dist)

            currentMin = float('inf')
            for i in range(len(points)):
                if i in visited:
                    continue
                if minDist[i] < currentMin:
                    currentMin = minDist[i]
                    index = i
        return sum(minDist)
