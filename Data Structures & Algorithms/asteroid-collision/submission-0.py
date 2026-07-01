class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                #handling collisions. if diff < 0, stack[-1] < a
                if diff < 0:
                    stack.pop()
                
                #or stack[-1] > a, set a to zero to end the loop
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    stack.pop()

            if a:
                stack.append(a)
                
        return stack












        # #have a stack 
        # # add to the stack if in the same direction as top, compare if in opposite direction to explode
        # stack = []
        # for a in asteroids:
        #     if stack:
        #         if (stack[-1] < 0 and a < 0) or (stack[-1]> 0 and a > 0):
        #             stack.append(a)
        #         else:
        #             if stack[-1] <= a:
        #                 stack.pop()
        #                 stack.append(a)
        #     else:
        #         stack.append(a)
        # return stack