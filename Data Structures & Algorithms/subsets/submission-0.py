class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []

        def dfs(i):
            #base case if we reach out of bounds, add a copy of the current subset to res 
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            #include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            #exclude nums[i] 
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
        # res = []
        # path = []
        # def dfs(i):
        #     if i >= len(nums):
        #         res.append(path.copy())
        #         return 
        #     path.append(nums[i])
        #     dfs(i+1)
        #     path.pop()
        #     dfs(i + 1)
        # dfs(0)
        # return res

                
        

        