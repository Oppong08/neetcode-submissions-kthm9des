class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #nums = [3,4,5,6,1,2], target = 1

        #logic:for a rotated sorted array check whether target is in the left larger sorted part of the pivot(mid)
        #or target is in the lesser rigth sorted half before ajusting pointers
        
        l,r = 0, len(nums) -1
        while l <= r:
            m = (l+r)//2
            #first case: if m is the target
            if nums[m] == target:
                return m
            
            #if were in left larger sorted half about the pivot and
            if nums[l] <= nums[m] :
                #if target is target is bigger than mid or smaller than the left-most item 
                #then we need to search the right half or right of the left half
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else: #meaning target is less than middle but greater than the leftmost
                    r = m -1 
            #if were in right half and
            else:
                #if  target is less than mid or bigger than rightmost value
                if target < nums[m] or target > nums[r]:
                 #then we should search in the left side 
                    r = m - 1
                else: #target is bigger than the middle and less than the rightmost value 
                    #target #or left side of the right half
                    l = m + 1
        
        return -1


