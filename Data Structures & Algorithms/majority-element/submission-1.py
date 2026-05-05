class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Boyer-More algorithm(since we're guaranteed a majority element)
        res, count = 0,0

        for n in nums:
            if count == 0:
                res = n

            count += 1 if n == res else -1
        return res


















        # #simple
        # count = {}
        # res, maxCount = 0, 0 
        # for n in nums:
        #     count[n] = 1 + count.get(n,0)
        #     res = n if count[n] > maxCount else res
        #     maxCount = max(count[n], maxCount)
        # return res
               
        
        # for n in nums:
        #     if count[n] > len(nums)/2:
        #         return  n