class Solution:
    def validPalindrome(self, s: str) -> bool:
        #optimal two pointers
        l,r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l + 1 : r+1], s[l :r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]

            l, r = l+1 , r-1

        return True







        # def isPalindrome(word):
        #     return word == word[::-1]
        
        # for i in range(len(s)):
        #     if isPalindrome(s[:i] + s[i+1:]):
        #         return True
        # return False
    
    

        
