class Solution:
    def countSubstrings(self, s: str) -> int:
        #check each substring for palindrome, increase count
        res = 0
        
        i = 0 
        for i in range(len(s)):
            l, r = i, i 
            while l > 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -=1
                r += 1

            l, r = i, i+1
            while l > 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -=1 
                r += 1
            
        return res

        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         l,r = i, j
        #         while l < r and r < len(s) and s[l] == s[r]:
                     
        #             l += 1
        #             r -= 1
        #         res += (l >= r)
        # return res
