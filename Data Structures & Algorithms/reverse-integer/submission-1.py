class Solution:
    def reverse(self, x: int) -> int:
        #core idea: build the reverse digit by digit by repeatedly taking the last digit of the number, 
        #append to the end of a running res then remove the last digit from the orginal number
        #before updating res, check for overflow

        MIN = -2147483648 
        MAX = 2147483647

        res = 0
        while x:
            digit = int(math.fmod(x,10)) #extract the last digit
            x = int(x/10)    #remove the last digit

            #check for overeflow
            if res > MAX//10 or (res == MAX//10 and digit > MAX % 10):
                return 0
            
            if res< MIN//10 or (res == MIN//10 and digit < MIN % 10):
                return 0
            
            #update res
            res = (res*10) + digit
        
        return res

























        # MIN = -2147483648   #interger. MAX_VALUE (-2 ^ 31) 
        # MAX = 2147483647     #Integer.MIN_VALUE (2 ^ 31 - 1)

        # res = 0
        # while x:

        #     digit = int(math.fmod(x,10))
        #     x = int(x/10)

        #     if (res > MAX //10 or 
        #         (res == MAX//10 and digit >= MAX % 10)):
        #         return 0
        #     if (res < MIN//10 or 
        #         (res == MIN//10 and digit <= MIN %10)):
        #         return 0
        #     res = (res * 10) + digit

        # return res

