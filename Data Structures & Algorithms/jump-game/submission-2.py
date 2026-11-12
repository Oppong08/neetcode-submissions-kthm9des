class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #greedy:
        #logic: initialize end goal position to be at the last end(len(nums)-1)
        #loop through backwards, at each index i, check if the maximimum jump nums[i] can reach the end goal position
        #if it can, update end goal position to current index, else return False immediately
        #return True if end goal is able to reach starting position(index 0)'
        goal = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal: #if we can reach current goal from here, make here the current goal
                goal = i
        return True if goal == 0 else False






        # rem = nums[0]
        # i = 1
        # while i+1 < len(nums):
        #     rem = max(rem-1, nums[i])
        #     if nums[i + 1] > rem:
        #         return False
        #     i += 1
        # return True
                
        