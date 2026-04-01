class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #logic: loop through s backwards, at each index(substring), 
        #check if any of the words in the word dict can be formed from that index to end can be marked as 
        # have a dp array mark i and i + w as true indicating a valid word break, continue until index 0
        dp = [False] * (len(s) + 1)

        dp[len(s)] = True #the empty string is a valid segmentation

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]

                #if at leas one word from the wordict can be formed starting from i, no need to check other words, hence break
                if dp[i]: 
                    break
        return dp[0]
            














        # #my logic: loop through the string until you find a substring in the dictionary, start a new search after found, continue to the end 
        # #return true if all substring are in the dictonary

        # res = False
        # i = 0
        # for j in range(i, len(s)):
        #     if j < len(s) and s[i:j] not in wordDict:
        #         continue
        #     if s[i:j] in wordDict:
        #         i = j + 1
        #         res = True
        #     else:
        #         res = False
        # return res
            
        
            
