class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Brute force loop through each subarray, calculate product, update max
        res = nums[0]
        for i in range(len(nums)):
            cur = nums[i]
            res = max(res, cur)
            for j in range(i + 1, len(nums)):
                cur *= nums[j]
                res = max(res, cur)

        return res
        



    #dp optimal 
    #Core logic:  single loop, use curmax and curmin to track maximum product ending at each index
    #at each index, we update curmax and curmin by including the current number (num * curmax), (num * curmin) and n
    #result is then updated with the current maximum product ending at that index 

        curMax, curMin = 1, 1  #curMin and curMax initiated with 1 to make it neutral
        res = nums[0]
        for num in nums:
            tmp = curMax
            curMax = max(nums * curMax, nums * curMin, num) #curMin included since a flip in sign from - to + could possibly change the curMax
            curMin = min(tmp * num, nums * curMin, num)
            res = max(res, curMax)
        
        return res




















        # res = nums[0]
        # curMin, curMax = 1, 1

        # for num in nums:
        #     tmp = curMax * num
        #     curMax = max(num * curMax, num * curMin, num)
        #     curMin = min(tmp, num * curMin, num)

        #     res = max(res, curMax)

        # return res