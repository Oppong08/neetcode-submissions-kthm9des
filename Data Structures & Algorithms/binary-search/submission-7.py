class Solution:
    #recursive
    # def binary_search(self, l: int, r: int, nums: List[int], target: int) -> int:
    #     if l > r:
    #         return -1 
        
    #     mid = l + ((r-l)//2)
    #     if nums[mid] == target:
    #         return mid
    #     if nums[mid] < target:
    #         return self.binary_search(l+1,mid,target, nums)
    #     return self.binary_search(l, mid-1,  target, nums)
      
    def search(self, nums: List[int], target: int) -> int:
        # return self.binary_search(0, len(nums)-1, nums, target)
        #iterative
        if len(nums) == 1:
            return 0 if nums[0]== target else -1
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = l + ((r-l)//2)
            if nums[mid] < target:
                l +=1
            elif nums[mid] > target:
                r -= 1
            else:
                return mid
        return -1

        #recursive
        #base case: if the search window is empty.ie if l > r:
       




