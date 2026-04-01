class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #dynamic programming: concept(at each step in the array, our maximum )
        # is the maximum between the ( robbing current item and calculated max's until 
        #the previous two items) or the maximum up untill the array before excluding the current

        #eg[rob1, rob2, n, n+1, n+2] #
        rob1 = 0 # the max money up to two houses ago
        rob2 = 0 # he max money up to the previous house

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2








        #recursive
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     return max(dfs(i + 1),
        #                nums[i] + dfs(i + 2))

        # return dfs(0)
         

        