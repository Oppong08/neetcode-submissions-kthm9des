class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #state: (i, Buying or selling?)
        #at each state, we can decide to take action or cooldown depenging on whether we're buying/selling
        #if buy -> move to the next((i + 1), subtract prices[i]
        #if sell -> skip the next (i + 2), add prices[i]

        dp = {} #dp i stores maximum profit we can make starting from index[i]

        def dfs(i, buying):
            #base case, at last index, 0 profit can be made
            if i >=len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i,buying)]
            
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i,buying)] = max(buy, cooldown)
            
            else:
                sell = dfs(i+2, not buying) + prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i,buying)] = max(sell, cooldown)
            
            return dp[(i,buying)]
        
        return dfs(0, True)





        # dp = {} #key = (i, buying)  val = max_profit

        # def dfs(i, buying):
        #     if i >= len(prices):
        #         return 0

        #     if (i, buying) in dp:
        #         return dp[(i, buying)]

        #     if buying:
        #         buy = dfs(i + 1, not buying) - prices[i]
        #         cooldown = dfs(i + 1, buying)
        #         dp[(i, buying)] = max(buy, cooldown)
        #     else:
        #         sell = dfs(i + 2, not buying) + prices[i]
        #         cooldown = dfs(i+1, buying)
        #         dp[(i, buying)] = max(sell, cooldown)
            
        #     return dp[(i, buying)]
        
        # return dfs(0, True)

