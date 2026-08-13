class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #two pointers, find the first positive, loop till the last, return missing
        #optimized: #possible solution set (1, len(nums) + 1)
        #mark all negative values as 0
        # for i in range(len(nums)):
        #     if nums[i] < 0:
        #         nums[i] = 0
        
        # #mark existing in bound values in the array as negative
        # for i in range(len(nums)):
        #     val = abs(nums[i])
        #     if i <= val <= len(nums):
        #         if nums[val - 1] > 0:
        #             nums[val - 1] *= -1
        #         elif nums[val-1] == 0:
        #             nums[val -1] = -1 * (len(nums) + 1)
        # #loop through from 1, to len(nums) + 1, to find missing positive
        # for i in range(1, len(nums) + 1):
        #     if nums[i-1] >= 0:
        #         return i

        # return len(nums) + 1


        

        #sorting
        nums.sort()
        missing = 1
        for n in nums:
            if n > 0 and n == missing:
                missing += 1
        return missing



        #bruteforce
        # nums.sort()
        # i = 1
        # while i > 0 and i in nums:
        #     i += 1
        # return i
        
       