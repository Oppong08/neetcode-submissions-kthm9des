class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #my logic: loop through the string until you find a substring in the dictionary, start a new search after found, continue to the end 
        #return true if all substring are in the dictonary

        res = False
        i = 0
        for j in range(i+1, len(s)):
            if j < len(s) and s[i:j] not in wordDict:
                continue
            if s[i:j] in wordDict:
                i = j + 1
                res = True
            else:
                res = False
        return res
            
        
            
