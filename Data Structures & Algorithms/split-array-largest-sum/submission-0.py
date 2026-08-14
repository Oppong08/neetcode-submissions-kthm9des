class Solution:
    def splitArray(self, nums: List[int], k: int) -> int: 
        #bruteforce: try spliting into two based on each index, calculate the sum and record the minimum (recursion)
        def canSplit(largest):
            subarray = 1
            curSum = 0
            for num in nums:
                curSum += num
                if curSum > largest:
                    subarray += 1
                    if subarray > k:
                        return False
                    curSum = num
            return True

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = l + (r - l) // 2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
        #binary search(n log s)
        # l, r = max(nums), sum(nums) #possible minimum and maximum answers
        # res = r
        # def canSplit(largest):
        #     subarray = 1
        #     curSum = 0
        #     for n in nums:
        #         curSum += n 
        #         if curSum > largest:
        #             subarray += 1
        #             curSum = n
        #     return subarray + 1 <= n

        # while l <= r:
        #     mid = l + ((r-l)//2)
        #     if canSplit(mid):
        #         res = mid
        #         r = mid - 1
        #     else:
        #         l = mid + 1
                 
        # return res