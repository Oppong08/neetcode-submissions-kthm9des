class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #two pointers, find the first positive, loop till the last, return missing
        nums.sort()
        i = 1
        while i > 0 and i in nums:
            i += 1
        return i
        
        # nums = nums.sort()
        # first = 0
        # for num in nums:
        #     if num > 0:
        #         first = num
        # last = nums[-1]
         
        # for n in range(first, last):
        #     if n not in nums:
        #         return n
