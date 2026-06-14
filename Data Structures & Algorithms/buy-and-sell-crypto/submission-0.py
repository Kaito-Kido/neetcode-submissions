class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]
        
        for p in prices:
            maxProfit = max(maxProfit, p - minBuy)
            minBuy = min(minBuy, p)
        
        return maxProfit