class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gasTotal = 0
        costTotal = 0
        for g in gas:
            gasTotal += g
        
        for c in cost:
            costTotal += c

        if costTotal > gasTotal:
            return -1
        
        accumulate = 0
        currentIndex = 0
        while currentIndex < len(cost):
            j = currentIndex
            while accumulate >= 0 and j < len(cost):
                accumulate += gas[j] - cost[j]
                j += 1
            
            if j == len(cost) and accumulate >= 0:
                return currentIndex
            else:
                currentIndex = j
                accumulate = 0
        return -1

            

        