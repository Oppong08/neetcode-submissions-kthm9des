class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #dfs bottom up 
        
        dp = [(amount + 1) for i in range(amount + 1)]

        dp[0] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a]= min(dp[a], 1 + dp[a - coin])
            
        return dp[amount] if dp[amount] != amount + 1 else - 1


















        #dfs top-down
        # memo = {}
        # def dfs(amount):
        #     if amount == 0: 
        #         return 0
            
        #     if amount in memo: 
        #         return memo[amount]
            
        #     res = 1e9

        #     for coin in coins:
        #         if amount - coin >= 0:
        #             res = min(res, 1 + dfs(amount - coin))
            
        #     memo[amount] =res
        #     return memo[amount]
        
        # mincoin = dfs(amount)
        # return -1 if mincoin >= 1e9 else mincoin
        