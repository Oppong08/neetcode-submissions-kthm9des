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
        #     r += 1
            
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
        # for i in range(len(s)):
        #     for j in range(i,len(s)): #check palindrome at each j (substring)
        #         l, r = i, j # i and j mark current substring, l,r to check palindrome
            
        #         while l < r and r < len(s) and s[l] == s[r]:
        #             l += 1
        #             r -=1
                
        #         if l >= r and (j - i + 1) > resLen: # if we've found a substring palindrome longer than curent
        #             res = s[i:j + 1]
        #             resLen = j-1 + 1
        # return res

        #dp
        #logic: uses a 2d matrix as dp array, fills the matrix from bottom to up(i), left to right(j)
        #checks for palindrom in each substring in the loop(i -> j) by checking the end characters(i,j) as well as inner words(dp[i+1][j-1]), updates result and matrix values accordingly
        #dp[i][j] is the position of a character in the n x n dp matrix

        resIdx = 0#helps us to find starting index of the palindromic substring at the end
        resLen = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)] #n x n dp matrix

        for i in range(n-1, -1, -1): #i loops through the string backwards, fill the matrix from bottom to top
            for j in range(i, n): #j loops through the substring from left to right starting from i, fills the matrix from left to right starting from i
    #palindrome condition: if last characters are the same and the length of the substring is <= 2(they are palindromes) or inner characters have been marked as palindromes on the dp matrix(dp[i+1][j-1])
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True

    #update the curr res and reslength if new palindromic substring longer than the current one
                    if resLen < (j-i + 1):
                        resIdx = i
                        resLen = j - i + 1
        return s[resIdx: resIdx + resLen]


        



                

