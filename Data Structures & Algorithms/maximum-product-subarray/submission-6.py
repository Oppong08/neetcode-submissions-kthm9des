class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Brute force loop through each subarray, calculate product, update max
        # res = nums[0]
        # for i in range(len(nums)):
        #     cur = nums[i]
        #     res = max(res, cur)
        #     for j in range(i + 1, len(nums)):
        #         cur *= nums[j]
        #         res = max(res, cur)

        # return res
        



    #dp optimal 
    #Core logic:  single loop, use curmax and curmin to track maximum product ending at each index
    #at each index, we update curmax and curmin by including the current number (num * curmax), (num * curmin) and n
    #result is then updated with the current maximum product ending at that index 

        # curMax, curMin = 1, 1  #curMin and curMax initiated with 1 to make it neutral
        # res = nums[0]
        # for num in nums:
        #     tmp = curMax       #store old curMax before updating 
        #     curMax = max(nums * curMax, nums * curMin, num) #curMin included since a flip in sign from - to + could possibly change the curMax
        #     curMin = min(tmp * num, nums * curMin, num)
        #     res = max(res, curMax)
        
        # return res




        #prefix & suffix: NB: each number at index i is either part of the running prefix product or running suffix product
        #logic: loop through the array, at each index compute prefix (running product up from left to right) and suffix(running product from right to left)
        #res is then the max of (nums[i], max(prefix, suffix))

        res = nums[0]
        prefix = suffix = 0
        for i in range(len(nums)):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[len(nums)-1-i] * (suffix or 1)
            res = max(res, max(prefix, suffix))
        return res








        # res = nums[0]
        # curMin, curMax = 1, 1

        # for num in nums:
        #     tmp = curMax * num
        #     curMax = max(num * curMax, num * curMin, num)
        #     curMin = min(tmp, num * curMin, num)

        #     res = max(res, curMax)

        # return res