class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            
            new = str(n)
            n =int(new[0])**2
            for i in range(1,len(new)):
                n += int(new[i]) ** 2
            
            if n in seen:
                return False
            seen.add(n)
            
        return True
            

            
                