class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i + 1, len(nums) -1 
            while j < k:
                if nums[j] + nums[k] + nums[i]< 0:
                    j += 1
                elif nums[j] + nums[k] + nums[i] > 0 :
                    k-=1 
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j]== nums[j-1] and j<k:
                        j += 1
        
        return res




























        # res = []
        # nums.sort()
        # for i, a in enumerate(nums):
        #     if i > 0 and a == nums[i-1]:
        #         continue
        #     l = i+1
        #     r = len(nums)-1
        #     while l < r:
        #         triplet = a + nums[l] + nums[r] 
        #         if triplet > 0:
        #             r-= 1
        #         elif triplet < 0:
        #             l +=1
        #         else:
        #             res.append([a,nums[l],nums[r]])
        #             l+=1
        #             while nums[l] == nums[l-1] and l < r:
        #                 l +=1

        # return res



            




























        


            

        