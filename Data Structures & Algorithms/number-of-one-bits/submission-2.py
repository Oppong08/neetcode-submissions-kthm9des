class Solution:
    def hammingWeight(self, n: int) -> int:
        # res = 0

        # while n:
        #     res += n % 2
        #     n = n >> 1
        # return res
        
                
        #Bit Mask - 1
        #logic: loop through n, at each position, create a mask with a single 1 at that position using 1<<i
        #Use bitwise  AND(&) to test whether that bit is set in n and update a counter accordingly
        # res = 0
        # for i in range(32):
        #     if (1 << i) & n:
        #         res+=1
        # return res

        #Bit mask II 
        #logic: Instead of checking every bit position explicitly, we can:
        #look at the least signifcant bit of n(right most value)
        #shifting n right by one (n >>= 1) moves us to the next bit
        #we repeat the process until n becomes 0

        res = 0
        while n:
            if n & 1:
                res+=1 
            else:
                res+=0
            n >>= 1
        return res