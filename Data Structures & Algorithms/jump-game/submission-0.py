class Solution:
    def canJump(self, nums: List[int]) -> bool:
        rem = nums[0]
        i = 1
        while i+1 < len(nums):
            rem = max(rem-1, nums[i])
            if nums[i + 1] > rem:
                return False
            i += 1
        return True
                
        