class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #no division
        #logic: for each number, the desired multiple is the multiple of 
        #all numbers before it(prefix) and the numbers after it(suffix) 
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)) :
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for j in range(len(nums)-1,-1, -1):
            res[j] *= suffix
            suffix *= nums[j]
        return res



        # #division: 
        # res = []
        # total = 1 
        # for i in nums:
        #     total *= i
        # for j in nums:
        #     res.append((total//j)if j != 0 else 0)
        # return res

        #Brute force
        # res = []
        # i = 0 
        # while i < len(nums):
        #     multiple = 1
        #     j= 0 
        #     while j < len(nums):
        #         if j != i:
        #             multiple *= nums[j]
        #             j += 1
        #         else:
        #             j+=1 
        #     res.append(multiple)
        #     i += 1
        #return res


