class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #recursive + optimized
        dp = {}
        def dfs(i,j):
            if j == len(t):
                return 1

            if i == len(s):
                return 0
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            if s[i] == t[j]:
                dp[(i,j)] = dfs(i+1,j+1) + dfs(i+1, j)
            else:
                dp[(i,j)] = dfs(i+1, j)
            return dp[(i,j)]
            
        return dfs(0,0)
































        # if len(t) > len(s):
        #     return 0
        # cache = {}

        # def dfs(i,j):
        #     if j== len(t):
        #         return 1
        #     if i == len(s):
        #         return 0
        #     if (i,j) in cache:
        #         return cache[(i,j)]

        #     if s[i] == t[j]:
        #         cache[(i,j)] = dfs(i+1, j+1) + dfs(i + 1, j)
        #     else:
        #         cache[(i,j)] = dfs(i + i, j)
        #     return cache[(i,j)]
        # return dfs(0, 0)
    
        # if len(t) > len(s):
        #     return 0

        # dp = {}
        # def dfs(i, j):
        #     if j == len(t):
        #         return 1
        #     if i == len(s):
        #         return 0
        #     if (i, j) in dp:
        #         return dp[(i, j)]

        #     res = dfs(i + 1, j)
        #     if s[i] == t[j]:
        #         res += dfs(i + 1, j + 1)
        #     dp[(i, j)] = res
        #     return res

        # return dfs(0, 0)

        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

        return dp[0][0]

