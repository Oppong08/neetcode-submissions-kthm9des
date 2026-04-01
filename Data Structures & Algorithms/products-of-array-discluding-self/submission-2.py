class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #no division
        #logic: for each number, the desired multiple is the multiple of 
        #all numbers before it(prefix) and the numbers after it(suffix) 
        res = []
        prefix = 1
        for i in range(len(nums)):
            res.append(prefix)
            prefix = nums[i] * prefix
        suffix = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] *= suffix
            suffix = nums[j] * suffix
        return res
            

























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
        # prod = 1
        # zero_cnt = 0 
        # for i in nums:
        #     if i:
        #         prod *= i 
        #     else:
        #         zero_cnt+= 1
           
        # if zero_cnt > 1: #all other multiplications 
        # #would involve multiplying by that zero and would result in a zero
        #     return [0] * len(nums)
        # res = [0] * len(nums)
        # for i, v in enumerate(nums):
        #     if zero_cnt: #at least one zero: meaning all other multiples would involve zero
        #     #except the value 0 itself 
        #         res[i] = 0 if v else prod
        #     else:
        #         res[i] = prod // v
        #     return res

            

        

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


