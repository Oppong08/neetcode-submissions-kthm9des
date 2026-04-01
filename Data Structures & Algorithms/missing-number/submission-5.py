class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # #sorting
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] != i:
        #         return i
        # return len(nums)

        #hash set
        num_set = set(nums)
        for i in range(len(nums)+1):
            if i not in num_set:
                return i