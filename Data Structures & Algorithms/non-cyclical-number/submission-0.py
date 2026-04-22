class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            new = str(n)
            n =int(new[0])**2
            for i in range(1,len(new)):
                n += int(new[i]) ** 2
            seen.add(n)
            
        return True
            

            
                