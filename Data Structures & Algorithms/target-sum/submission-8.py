class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # #bruteforce (recursive)
        # def dfs(i,total):
        #     if i == len(nums):
        #         if total == target:
        #             return 1
        #         else:
        #             return 0
            
        #     return dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
        
        # return dfs(0,0)

        #memoized
        memo = {}
        def dfs(i, total):
            if (i,total) in memo:
                return memo[(i,total)]
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
        
            
            memo[(i,total)] = dfs(i + 1, total+nums[i]) + dfs(i + 1, total - nums[i])
            return memo[(i,total)]
        
        return dfs(0,0)

            
            




































        # #2d array
        # dp = [defaultdict(int) for _ in range(len(nums)+ 1)]

        # dp[0][0] = 1 #(0 elements used, 0 sum) -> 1 way

        # for i in range(len(nums)):
        #     for cur_sum, count in dp[i].items():
        #         dp[i+1][cur_sum + nums[i]] += count
        #         dp[i+1][cur_sum - nums[i]] += count
        
        # return dp[len(nums)][target]















        # # Bruteforce recursive
        # dp = {} #(i,total) -> num of ways

        # def dfs(i,total):
        #     if (i,total) in dp:
        #         return dp[(i,total)]

        #     if i == len(nums):
        #         if total == target:
        #             return 1
        #         else:
        #             return 0
            
        #     dp[(i,total)] = dfs(i + 1, total + nums[i]) + dfs(i+1, total - nums[i])
        #     return dp[(i,total)]
        
        # return dfs(0,0)
            