class Solution:
    def isHappy(self, n: int) -> bool:
        # seen = set()
        # while n != 1: 
        #     new = str(n)
        #     n =int(new[0])**2
        #     for i in range(1,len(new)):
        #         n += int(new[i]) ** 2
            
        #     if n in seen:
        #         return False
        #     seen.add(n)
            
        # return True
            
        
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n== 1:
                return True
        
        return False
    
    def sumOfSquares(self, n):
        output = 0

        while n:
            digit = n%10
            digit= digit **2
            output += digit
            n = n//10
        return output

            
                