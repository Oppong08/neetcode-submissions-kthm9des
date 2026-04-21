class Solution:
    def checkValidString(self, s: str) -> bool:

        # leftMin, leftMax = 0, 0

        # for c in s:
        #     if c == "(":
        #         leftMin, leftMax = leftMin + 1, leftMax + 1
            
        #     if c == ")":
        #         leftMin, leftMax = leftMin - 1, leftMax - 1
            
        #     else:
        #         leftMin, leftMax = leftMin - 1, leftMax + 1

        #     if leftMax < 0:
        #         return False
            
        #     if leftMin < 0 : #s = (*)(
        #         leftMin = 0
        
        # return leftMin == 0

        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0




















        # total = 0
        # opened, closed, star = 0,0, 0
        # for i in s:
        #     if i == "(":
        #         total += 1
        #         opened += 1
        #     elif i == ")":
        #         total -= 1
        #         closed += 1
            
        #     else:
        #         star += 1
        
        # if total < 0 :
        #     total += star
        # else:
        #     total -= star

                
        # return total == 0