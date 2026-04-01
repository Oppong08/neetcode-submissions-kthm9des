class Solution:
    def rob(self, nums: List[int]) -> int:
        #logic: write the solution for house robber 1 without the circular constraint as a helper function
        # and run it on the circular conditions(the first and last houses are adjacent).
        # this done by running it on nums [i:](not include first house) and nums[:-1](include first house)
        # The max is the results
        
        #dp optimized
       #return max(nums[0],self.helper(nums[1:]), self.helper(nums[:-1])) #nums[0] included in the max determination in case the input is contain just 1 house
    
    # def helper(self, new_list):
    #     rob1, rob2 = 0, 0

    #     for n in new_list:
    #         curr = max(n + rob1, rob2)
    #         rob1 = rob2
    #         rob2 = curr
    #     return rob2

    #dp bottom up
        if len(nums)==1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))


    def helper(self, new_list):
        if not new_list:
            return 0
        if len(new_list)== 1:
            return new_list[0]
    
        dp = [0] * len(new_list)

        dp[0],dp[1] = new_list[0], max(new_list[0],new_list[1])
        for i in range(2,len(new_list)):
            dp[i] = max(new_list[i] + dp[i-2], dp[i-1])
        return dp[-1]




        