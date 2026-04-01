class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for i in s.lower():
            if i != " " and i.isalnum():
                s1 +=i
        l,r = 0, len(s1)-1
        while l < r:
            if s1[l] != s1[r]:
                return False
            l+=1
            r-=1
        return True
            
        
            
