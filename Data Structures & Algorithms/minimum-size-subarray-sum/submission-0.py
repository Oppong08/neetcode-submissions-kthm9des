class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #bruteforce: check every subarray > target, return minimum length
        # res = 0
        # total, count = 0, 0
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if total >= target:
        #             break
                
        #         total += nums[i]
        #         count += 1
        #         res = min(res, count)
        # return res
    
        window = set()
        l = 0 
        res = float("inf")
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r-l + 1)
                total -= nums[l]
                l += 1
            
        return res if res!= float("inf") else 0
            

