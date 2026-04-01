class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #logic: create a dp cache to store longest subsequence starting from index[i:] in the cache
        #loop through backwards , at eachh index i, move left to right with j, updating lis[i] if nums[j] is greater than
        # the longest subsequence at i is the max of dp[i] or adding nums[i] to the max of the sequence before it (max(cache[i], 1 + cache(j)))

        # dp = [1] * len(nums) 
    
        # for i in range(len(nums), -1, -1):
        #     for j in range(i, len(nums)):
        #         if nums[i] < nums[j]:
        #             dp[i] = max(dp[i], 1 + dp[j])
        # return max(dp)


       #dfs topdown:

        def dfs(i,j) :
            if i == len(nums):
                return 0
            
            LIS = dfs(i+1, j)

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i))

            return LIS
        
        return dfs(0,-1)











        # #bruteforce
        # res = 0
        # for i in range(len(nums)):
        #     count = 1
        #     for j in range(i+1, len(nums)):
        #         if nums[i] <= nums[j]:
        #             continue
        #         if nums[i] > nums[j]:
        #             count += 1
        #             res= max(res, count)
        # return res