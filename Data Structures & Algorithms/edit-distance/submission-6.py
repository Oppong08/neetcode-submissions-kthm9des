class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        # n = len(word2)
    #     def dfs(i,j):
    #     #base case1: if we reach the end of word1, all remaning characters in word 2 must be inserted(insert n-j)
    #         if i == m:
    #             return n - j
    #     #base case2: if we reach the end of word2, all remaining characters in word 1 must be deleted
    #         if j == n:
    #             return m - i
            
    #         if word1[i] == word2[j]:
    #             return dfs(i + 1, j + 1)
            
    #         # res = min(dfs(i+1, j), dfs(i,j+1))
    #         # res = min(res, dfs(i+1,j+1))
    #         # return res + 1
    #         insert = dfs(i, j + 1)
    #         remove = dfs(i+1, j)
    #         replace = dfs(i + 1, j+ 1)
    #         return 1 + min(insert, remove, replace)
            
    #     return dfs(0,0)


    #dp bottom up
    #create 2D DP table(m+1 x n+1)
    # dp = [[float("inf")] * n+1 for i in range(m+1)]

        cache = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]
        
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+ 1][j+1]
                
                else:                    #delete          #insert           #replace
                    cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])

        return cache[0][0]