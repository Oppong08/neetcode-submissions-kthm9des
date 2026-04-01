class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        i = 0 
        while i < len(nums):
            multiple = 1
            j= 0 
            while j < len(nums):
                if j != i:
                    multiple *= nums[j]
                    j += 1
                else:
                    j+=1 
            res.append(multiple)
            i += 1
        return res


