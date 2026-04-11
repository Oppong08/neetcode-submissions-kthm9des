class Solution:
    def findMin(self, nums: List[int]) -> int:
        #logic: in an unrotated sorted array, the left most is the least
        #after rotating, both parts around a pivot are sorted, with left half containing greater values sorted left to rigth
        # and right half containing lower values sorted right to left 
        #determine where pivot falls (in the left larger or right lower), do binary search on the part containing the lower numbers

        res = nums[0]
        l, r = 0 , len(nums) - 1

        while l <= r:
            #case 1: if its unrotated, return minimum of res, and the leftmost value
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break
            #choose middle as pivot
            mid = (l+r)//2
            res = min(res, nums[mid])
            #if pivot falls within larger left part sorted from left to right and hence nums[mid] > nums[l]
            if nums[mid] > nums[l]:
                l = mid + 1
            else: #if pivot falls within the lower sorted part sorted rigth to left and hence nums[mid] < nums[l]
                r = mid - 1

        return res




        
        
