class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:   #if sum of nums is odd, partition not possible
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums)//2

        for i in range(len(nums)-1, -1, -1):
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        
        return True if target in dp else False


















        # #bruteforce: check each subset see if total equals half the sum
        # target = (sum(nums))/2
        # def dfs(i, total):
        #     if total == target:
        #         return True
        #     if i >= len(nums) or total > target:
        #         return False

        #     return dfs(i, total + nums[i]) or dfs(i + 1, total)

        # return dfs(0, 0)


