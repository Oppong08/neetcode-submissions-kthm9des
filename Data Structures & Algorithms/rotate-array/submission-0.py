class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - k

        while r < len(nums):
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r += 1