class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        taskcount = defaultdict(int)
        
        for task in tasks:
            taskcount[task] = taskcount[task] + 1
        
        for key, value in taskcount.items():
            heapq.heappush(heap, (-value, key))
        
        idlequeue = deque()
        cycle = 0
        while heap or idlequeue:
            cycle += 1
            if len(heap) != 0:
                value, task = heapq.heappop(heap)
                value = value + 1
                if value < 0:
                    if n > len(idlequeue):
                        for _ in range(n - len(idlequeue)):
                            idlequeue.append(-1)
                    idlequeue.append((value, task))
            if len(idlequeue) != 0:
                v = idlequeue.popleft()
                if v != -1:
                    heapq.heappush(heap, v)
            
        return cycle



