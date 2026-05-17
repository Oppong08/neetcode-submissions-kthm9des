class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # l, r = 0, 1
        # count = 0
        # total = 0
        # while r < len(nums):
        #     total = sum(nums[l:r])
        #     if total == k:
        #         count += 1
        #         l += 1
        #         r += 1
            
        #     else:
        #         if total > k:
        #             l += 1
        #         else:
        #             r+=1
        
        # return count


        res = 0
        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]
                if sum == k:
                    res += 1
        return res







        #brute force: extract all subarrays whose sum up to k
        # count = 0
        # for i in range(len(nums)):
        #     sum = nums[i]
        #     if sum == k:
        #         count +=1 
        #     for j in range(i+1, len(nums)):
        #         sum+= nums[j]
        #         if sum == k:
        #             count += 1
        # return count
