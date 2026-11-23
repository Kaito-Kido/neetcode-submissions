# BruteFoce
# Start with k, using dfs + backtracking to explore all possible path
# Track 

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        heap = []
        shortestPath = defaultdict(int)
        shortestPath[k] = 0
        heapq.heappush(heap, (0, k))

        adjList = defaultdict(list)
        for u, v, time in times:
            adjList[u].append((v,time))
        
        while heap:
            currentTime, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            for v, time in adjList[u]:
                if v in visited:
                    continue
                if v in shortestPath:
                    shortestPath[v] = min(shortestPath[v], currentTime + time)
                else:
                    shortestPath[v] = currentTime + time
                heapq.heappush(heap, (shortestPath[v], v))
        if len(shortestPath) != n:
            return -1
        networkdelay = 0
        for v in shortestPath.values():
            networkdelay = max(networkdelay, v)
        
        return networkdelay

        
        

