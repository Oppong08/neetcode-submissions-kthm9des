class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #bruteforce
        # res = nums[0]
        # for i in range(len(nums)):
        #     res = max(nums[i], res)
        #     total = nums[i]
        #     for j in range(i + 1,len(nums)):
        #         total+= nums[j]
        #         res= max(total, res)
        # return res

        #greedy:
        #logic: initialize current maximum to the first item in array and current sum to 0.
        #loop through array once, at each num in nums, if our current sum is negative, reset it to 0 else add the current num to cursum
        #update current max with each current sum

        # res = nums[0]
        # cur = 0
        # for i in range(len(nums)):
        #     if cur < 0:
        #         cur = 0
        #     cur+= nums[i]
        #     res = max(res,cur)
        # return res

        # curmin, curmax = 0,0
        # res = nums[0]
        # for i in range(len(nums)):
        #     tmp = curmax
        #     curmax = max(tmp + nums[i], nums[i],curmin + nums[i])
        #     curmin = min(tmp + nums[i], nums[i], curmin + nums[i])
        #     res = max(curmin, curmax)
        # return res
        





        res = nums[0]
        curMin, curMax = 0, 0

        for num in nums:
            tmp = curMax + num
            curMax = max(num + curMax, num +curMin, num)
            curMin = min(tmp, num + curMin, num)
            res = max(res, curMax)

        return res

        