class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = 1

        while left <= right:
            mid = (left + right) // 2
            hour = self.calculateEatingHour(mid, piles)
            if hour > h:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
    
    def calculateEatingHour(self, k, piles):
        h = 0
        for p in piles:
            h += p // k
            if p % k != 0:
                h += 1
        
        return h