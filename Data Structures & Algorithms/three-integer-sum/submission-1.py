class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res: List[List[int]] = []
        # nums.sort()
        # n = len(nums)

        # for i, a in enumerate(nums):
        #     if a > 0:  # after sorting, no triplet can sum to 0
        #         break
        #     if i > 0 and a == nums[i - 1]:  # skip same 'a'
        #         continue

        #     l, r = i + 1, n - 1
        #     while l < r:
        #         s = a + nums[l] + nums[r]
        #         if s < 0:
        #             l += 1
        #         elif s > 0:
        #             r -= 1
        #         else:
        #             res.append([a, nums[l], nums[r]])
        #             l += 1
        #             r -= 1
        #             # skip duplicates on both sides
        #             while l < r and nums[l] == nums[l - 1]:
        #                 l += 1
        #             while l < r and nums[r] == nums[r + 1]:
        #                 r -= 1
        # return res
#If you want, I can annotate it with print-debug lines to show pointer movement.

        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r-=1
                elif threesum < 0:
                    l +=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l +=1
                    while nums[l] == nums[l-1]and l < r:
                        l +=1
        
        return res


            

        