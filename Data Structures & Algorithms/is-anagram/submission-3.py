class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h1 = {}
        h2 = {}
        for i in range(len(s)):
            h1[s[i]] = 1 + h1.get(s[i], 0)
            h2[t[i]] = 1 + h2.get(t[i], 0)

        for j in s:
            if h1[j] != h2.get(j,0):
                return False
        return True
        
         
        # for i in s:
        #     if h1 and i in h1:
        #         h1[i] += 1
        #     h1[i] = 1

        
        # for j in t:
        #     if j not in h1:
        #         return False
        #     if h2 and j in h2:
        #         if h2[j] <= h1[j]:
        #             h2[j] +=1 
        #         else:
        #             return False
        #     h2[j] = 1
            
        return True