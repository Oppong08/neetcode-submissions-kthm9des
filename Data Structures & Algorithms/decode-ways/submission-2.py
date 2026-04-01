class Solution:
    def numDecodings(self, s: str) -> int:
        #logic: we are not building the actual decoded string, just counting the number of ways we can decode it
        #create a dp cache to store number of ways for decoding the current number of strings in consideration from i(dfs i means s[i:] in consideration)
        # run a dfs through the characters, return dp [taking current number as a single digit(i + 1)] or dp[taking it as a double character(i + 2)]


        #dp cache
        # dp = {len(s) :  1} #(the entire length of the input string will map to 1 as it is 1 way of decoding the string)

        # def dfs(i):
        #     if i in dp: #takes care of i == len(s) since it's already in the base case 
        #         return dp[i]
        #     if s[i] == '0': #string that starts with 0 cannot be decoded
        #         return 0
            
        #     #subproblem 1: taking each number as one digit ( 0 - 9)
        #     res = dfs(i + 1)

        #     #subproblem 2 : taking the number as a double digit and
        #     #first #(starts with 1, ie 0 - 9)

        #     if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i +1] in "01234567"):
        #         res += dfs(i + 2)
        #     dp[i] = res
        #     return res
        
        # return dfs(0)
        
        
        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and
                s[i + 1] in "0123456"
                ):
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)
                






























        # #Map each letter to a number, try possible valid combinations and update res
        # res = 0
        # alpha = "ABCDEFGHIJKLMNOPQRST"
        # dp = {c : 1 + ord(c)-ord('A') for c in alpha}
        
        # def dfs(i):
        #     if i == len(s):
        #         return 0
        #     dfs(i, res + 1)
        #     dfs(i + 1)

