class Solution:
    def rob(self, nums: List[int]) -> int:
        #logic: write the solution for house robber 1 without the circular constraint as a helper function
        # and run it on the circular conditions(the first and last houses are adjacent).
        # this done by running it on nums [i:](not include first house) and nums[:-1](include first house)
        # The max is the results
        
    #    return max(nums[0],self.helper(nums[1:]), self.helper(nums[:-1])) #nums[0] included in the max determination in case the input is contain just 1 house
    
    # def helper(self, new_list):
    #     rob1, rob2 = 0, 0

    #     for n in new_list:
    #         curr = max(n + rob1, rob2)
    #         rob1 = rob2
    #         rob2 = curr
    #     return rob2

    #dp Top-down
        if len(nums) == 1:
            return nums[0]  
        memo = [[-1] * 2 for _ in range(len(nums))]

        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums)-1):
                return 0
            
            if memo[i][flag] != -1:
                return memo[i][flag]
            
            memo[i][flag] = max(dfs(i+1, flag), nums[i] + dfs(i+2, flag or (i==0)))
            
            return memo[i][flag]
        return max(dfs(0, True), dfs(1, False))
        