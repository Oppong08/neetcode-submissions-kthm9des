class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # l, r = 0, len(nums)-1

        # while l <= r:
        #     mid = l + (r-l)//2
        #     if target == nums[mid]:
        #         return True

        #     if nums[l] < nums[mid]:
        #         if nums[l]<= target < nums[mid]:
        #             r = mid-1 
        #         else:
        #             l = mid +  1

        #     elif nums[l] > nums[mid]:
        #         if nums[mid] < target <= nums[r] :
        #             l = mid + 1
        #         else:
        #             r = mid-1
        #     else:
        #         l += 1

        # return False


        l,r = 0, len(nums) -1
        while l <= r:
            m = (l+r)//2
            #first case: if m is the target
            if nums[m] == target:
                return True
            
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
        
        return False













        # #Augmented binary search
        # l, r = 0, len(nums) - 1

        # while l <= r:
        #     m  = l + (r - l)//2
        #     if nums[m] == target: return True

        #     #if we're in the left portion
        #     if nums[l] < nums[m]:
        #         if nums[l] <= target < nums[m]:
        #             r = m - 1

        #         else:
        #             l = m + 1

        #     #if we're in the right portion
        #     elif nums[l] > nums[m]:
        #         if nums[m] < target <= nums[r]:
        #             l = m + 1
        #         else:
        #             r = m -1 

        #     else: #handle duplicate values nums[l] == nums[m], skip l until they're no duplicates 
        #         l += 1
        
        # return False










        # # l,r = 0, len(nums) -1
        # # while l <= r:
        # #     m = (l+r)//2
        # #     #first case: if m is the target
        # #     if nums[m] == target:
        # #         return True
            
        # #     #if were in left larger sorted half about the pivot and
        # #     if nums[l] <= nums[m] :
        # #         #if target is target is bigger than mid or smaller than the left-most item 
        # #         #then we need to search the right half or right of the left half
        # #         if target > nums[m] or target < nums[l]:
        # #             l = m + 1
        # #         else: #meaning target is less than middle but greater than the leftmost
        # #             r = m -1 
        # #     #if were in right half and
        # #     else:
        # #         #if  target is less than mid or bigger than rightmost value
        # #         if target < nums[m] or target > nums[r]:
        # #          #then we should search in the left side 
        # #             r = m - 1
        # #         else: #target is bigger than the middle and less than the rightmost value 
        # #             #target #or left side of the right half
        # #             l = m + 1
        
        # # return False