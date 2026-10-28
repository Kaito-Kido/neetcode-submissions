class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskcount = defaultdict(int)
        
        for task in tasks:
            taskcount[task] = taskcount[task] + 1
        
        maxcounttasks = 0
        nummaxcountasks = 0
        for value in taskcount.values():
            if value > maxcounttasks:
                maxcounttasks = value
                nummaxcounttasks = 1
            elif value == maxcounttasks:
                nummaxcounttasks += 1
        
        minlength = maxcounttasks + (maxcounttasks - 1)*n + nummaxcounttasks - 1

        return max(minlength, len(tasks))
        




