class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #greedy
        profit = 0

        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i - 1])
        
        return profit
        

        # l, r = 0, 1
        # best = 0
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r]- prices[l]
        #         best = max(best, profit)
        #     else:
        #         l = r
        #     r+= 1   
        # return  best













        # profit = 0
        # s = 0
        # i = 0
        # while i < len(prices):
        #     if prices[i] < prices[s]:
        #         s = i
        #     profit = max(profit, prices[i] - prices[s])
        #     i+=1 
        # return profit
