class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h = {}
        for i in s:
            h[i] = i
        
        for j in t:
            if j not in h:
                return False
        return True