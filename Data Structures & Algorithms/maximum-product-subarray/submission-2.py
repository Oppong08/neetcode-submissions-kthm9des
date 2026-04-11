class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Brute force loop through each subarray, calculate product, update max
        res = nums[0]
        for i in range(len(nums)):
            cur = 1
            #res = max(res, cur)
            for j in range(i, len(nums)):
                cur *= nums[j]
            res = max(res, cur)

        return res
            





















        # res = nums[0]
        # curMin, curMax = 1, 1

        # for num in nums:
        #     tmp = curMax * num
        #     curMax = max(num * curMax, num * curMin, num)
        #     curMin = min(tmp, num * curMin, num)

        #     res = max(res, curMax)

        # return res