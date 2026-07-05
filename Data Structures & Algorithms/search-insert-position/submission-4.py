class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #binary search
        # res = len(nums)
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
        return l
    
        # #linear search:
        # #logic: loop through the array, the index where the number is greater than or equal to target is where the target is or should've been
        # for i in range(len(nums)):
        #     if nums[i] >= target:
        #         return i
        # return len(nums)
            
