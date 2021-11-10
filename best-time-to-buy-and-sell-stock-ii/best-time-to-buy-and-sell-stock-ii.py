class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cur_purchase = -1
        for index in range(len(prices)):
            if cur_purchase == -1:
                if index == len(prices)-1:
                    return profit
                if prices[index] < prices[index+1]:
                    cur_purchase = prices[index]
                    continue
            else:
                if index == len(prices)-1:
                    if cur_purchase != -1:
                        return profit + (prices[index]-cur_purchase)
                if prices[index] > prices[index+1]:
                    profit += (prices[index]-cur_purchase)
                    cur_purchase = -1
        return profit
            
        