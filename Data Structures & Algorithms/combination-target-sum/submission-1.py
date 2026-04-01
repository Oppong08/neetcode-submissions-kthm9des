class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curpath, total):
            if i >= len(nums) or total > target:
                return
            if total == target:
                res.append(curpath.copy())
                return
            curpath.append(nums[i])
            dfs(i, curpath, total + nums[i])
            curpath.pop()
            dfs(i + 1, curpath, total)

        dfs(0,[],0)
        return res





































        
        # res = []
        # def dfs(i, cur, total):
        #     #base case: if the sum  == 16: add our pair
        #     if total == target:
        #         res.append(cur.copy())
        #         return 
        #     #if we go out of bounds, also stop
        #     if i >= len(nums) or total > target:
        #         return 
        #     cur.append(nums[i])
        #     dfs(i, cur, total + nums[i])
        #     cur.pop()
        #     dfs(i + 1, cur, total)

        # dfs(0,[],0)
        # return res





