class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #core idea: map each prefix sum to its count in a map and initiate a result counter
        #loop through the nums left to right, at each num, check if there is a prefix sum that could be removed to get k. add the count of that prefix sum to res counter 
        res = 0
        curSum = 0
        prefixSums = {0 : 1}  #{prefix sum : its frequency}

        for n in nums:
            curSum +=n 
            diff = curSum - k
            
            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        
        return res
















        #sliding window doesn't work because there could be negative elements
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

        # res = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i, len(nums)):
        #         sum += nums[j]
        #         if sum == k:
        #             res += 1
        # return res

