class Solution:
    def longestPalindrome(self, s: str) -> str:
        #logic: loop through the string, checking palindrome from the center outwards using two pointers
        #update the current res after each palindromic check

        res= "" #stores current longest palindrom
        resLen = 0 #stores lenght of current longest palindrome

        # #Check while current substring is still a palindrome for odd substring length
        # for i in range(len(s)):
        #     l, r = i, i
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         if (r-l +1) > resLen:
        #             res = s[l:r+1]
        #             resLen = r-l + 1
        #         l -=1
        #         r += 1
            
        # #Check while current substring is still a palindrome for even substring length
        #     l,r = i, i+1
        #     while l >= 0 and r < len(s) and s[l] == s[r]:
        #         if (r-l + 1) > resLen:
        #             res = s[l:r+1]
        #             resLen = r - l + 1
        #         l -=1 
        #         r +=1
        # return res

        #Brute force: Try every substring, check whether its a palindrome, compare to the res and update accordingly
        for i in range(len(s)):
            for j in range(i,len(s)): #check palindrome at each j (substring)
                l, r = i, j # i and j mark current substring, l,r to check palindrome
            
                while l < r and r < len(s) and s[l] == s[r]:
                    l += 1
                    r -=1
                
                if l >= r and (j - i + 1) > resLen: # if we've found a substring palindrome longer than curent
                    res = s[i:j + 1]
                    resLen = j-1 + 1
        return res



                

