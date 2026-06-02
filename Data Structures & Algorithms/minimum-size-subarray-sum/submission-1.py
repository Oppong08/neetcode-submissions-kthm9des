class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # bruteforce: check every subarray > target, return minimum length
        res = float("inf")
        
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total >= target:
                    res = min(res, j-i + 1)
                    break
            
                
        return res if res != float("inf") else 0
    
        # window = set()
        # l = 0 
        # res = float("inf")
        # total = 0
        # for r in range(len(nums)):
        #     total += nums[r]
        #     while total >= target:
        #         res = min(res, r-l + 1)
        #         total -= nums[l]
        #         l += 1
            
        # return res if res!= float("inf") else 0
            

