class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #brute force: extract all subarrays whose sum up to k
        count = 0
        for i in range(len(nums)):
            sum = nums[i]
            if sum == k:
                count +=1 
            for j in range(i+1, len(nums)):
                sum+= nums[j]
                if sum == k:
                    count += 1
        return count
