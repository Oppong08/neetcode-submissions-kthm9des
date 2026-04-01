class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #logic: loop through s backwards, at each index(substring), 
        #check if any of the words in the word dict can be formed from that index to end can be marked as 
        # have a dp array mark i and i + w as true indicating a valid word break, continue until index 0
        
        #dp[i] = True if the substring s[i:] can be segmented into words in the wordDict
        # dp = [False] * (len(s) + 1)

       
        # dp[len(s)] = True #the empty string is a valid segmentation

        # for i in range(len(s)-1, -1, -1):
        #     for w in wordDict:
        #         if i + len(w) <= len(s) and s[i: i + len(w)] == w:
        #             dp[i] = dp[i + len(w)]

        #         #if at leas one word from the wordict can be formed starting from i, no need to check other words, hence break
        #         if dp[i]: 
        #             break
        # return dp[0]
            
        #recursion

        memo = {}
        def dfs(i):
            if i == len(s):
                return True
            
            if i in memo:
                return memo[i]
            
            for w in wordDict:
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    if dfs(i + len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
            
        return dfs(0)

        # memo = {}

        # def dfs(i):
        #     # If we reached end, success
        #     if i == len(s):
        #         return True

        #     # Already solved this state
        #     if i in memo:
        #         return memo[i]

        #     # Try every word in the dictionary
        #     for w in wordDict:
        #         if i + len(w) <= len(s) and s[i : i + len(w)] == w:
        #         #if s.startswith(w, i):              # match at index i
        #             if dfs(i + len(w)):            # solve remainder
        #                 memo[i] = True
        #                 return True

        #     memo[i] = False                         # No segmentation works
        #     return False

        # return dfs(0)










        
            
        
            
