class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #logic: build a 2D dp matrix with text1 and text 2, loop through bottom up (left to right)
        #at each cell[i][j] (representing the longest common subsequence from here to the end), the value at that cell depends on whether character in text1(i) and character in text2(j) matches :
        # if they match then dp[i][j] is 1 + the longest common subsequence of their next characters(dp[i + 1][j+1])
        #if they dont match,dp[i][j] is the maximum between LCS of the next i and the current j (dp[i+1, j]) or the next j and the current i(dp[i,j+1])
        
        # dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # for i in range(len(text1)-1, -1, -1):
        #     for j in range(len(text2)-1,-1, -1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i+1][j+1]
        #         else:
        #             dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        # return dp[0][0]  

        #dp topdown 
        
        memo = {}

        def dfs(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]

            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + dfs(i+1, j+1)
            
            else:
                memo[(i,j)] = max(dfs(i+1,j), dfs(i, j+1))
            return memo[(i,j)]
        return dfs(0,0)
