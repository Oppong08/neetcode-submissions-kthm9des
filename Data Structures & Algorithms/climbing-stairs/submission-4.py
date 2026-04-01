class Solution:
    def climbStairs(self, n: int) -> int:

        countmap = {}
        def dfs(i):
            if i == n:
                return 1
            elif i > n:
                return 0
                #return i == n
            if i in countmap:
                return countmap[i]
            countmap[i] = dfs(i+1) + dfs(i+2)
            return countmap[i]
        return dfs(0)
        

        #dp
        # one, two = 1, 1 
        # for i in range(n-1):
        #     temp = one
        #     one = one + two
        #     two = temp
        # return one

        #recursive
        # def dfs(i):
        #     if i >=n:
        #         return i==n
            
        #     return dfs(i+1)+ dfs(i+2)
        
        # return dfs(0)
        #memoization
        #create a list to store already calculated steps
        # memo = [-1] * n
        # def dfs(i):
        #     if i >= n:
        #         return i==n
            
        #     if memo[i] != -1:
        #         return memo[i]

        #     memo[i] = dfs(i+1) + dfs(i+2)
        #     return memo[i]
        # return dfs(0)
        
        
        
        