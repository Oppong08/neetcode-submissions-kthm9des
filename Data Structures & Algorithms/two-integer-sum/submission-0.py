class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {} #keeps track of the previous differences
        for i,n in enumerate(nums):
            diff = target - nums[i]
            if diff in h:
                return[h[diff],i]
            h[n] = i
        

        