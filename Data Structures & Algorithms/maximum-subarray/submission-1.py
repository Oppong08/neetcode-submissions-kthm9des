class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #bruteforce
        res = nums[0]
        for i in range(len(nums)):
            #res = max(nums[i], res)
            total = 0
            for j in range(i,len(nums)):
                total+= nums[j]
                res = max(total, res)
        return res
        # dp = [num for num in nums]
        # for i in range(len(nums)-1, -1, -1):
        #     for j in range(i, len(nums)-1):
        #         dp[i] = max(nums[j] + dp[i + 1], dp[i])
        
        # return max(dp)

        