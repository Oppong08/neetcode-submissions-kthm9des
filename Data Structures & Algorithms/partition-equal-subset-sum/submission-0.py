class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #bruteforce: check each subset see if total equals half the sum
        target = (sum(nums))/2
        def dfs(i, total):
            if total == target:
                return True
            if i >= len(nums) or total > target:
                return False

            return dfs(i, total + nums[i]) or dfs(i + 1, total)

        return dfs(0, 0)


