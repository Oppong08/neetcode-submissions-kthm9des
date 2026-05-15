class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp
        profit = 0

        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i - 1])
        
        return profit
        













        # profit = 0
        # s = 0
        # i = 0
        # while i < len(prices):
        #     if prices[i] < prices[s]:
        #         s = i
        #     profit = max(profit, prices[i] - prices[s])
        #     i+=1 
        # return profit
