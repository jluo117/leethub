class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = None
        curMax = None
        maxProfit = 0
        for price in prices:
            if curMin == None:
                curMax = None
                curMin = price
            elif curMin > price:
                curMax = None
                curMin = price
            elif curMax == None:
                curMax = price
                maxProfit = max(curMax - curMin, maxProfit)
            elif curMax < price:
                curMax = price
                maxProfit = max(curMax - curMin, maxProfit)
        return maxProfit
        
        
