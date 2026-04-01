class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #logic: if an arry can be partitioned into 2 equal halves, there is a possible set of combination to reach half the sum of all numbers
        #A set containing all total possible sums of the items will contain the target

        # if sum of nums is odd, -> can't partition into 2
        if sum(nums)%2:
            return False
        target = sum(nums)/2
        dp = set() #dp set
        dp.add(0)

        for i in range(len(nums)-1, -1, -1):
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i]) #add number
                nextDP.add(t) #don't add number
            dp = nextDP
        
        return True if target in dp else False
            

























        # if sum(nums) % 2:   #if sum of nums is odd, partition not possible
        #     return False
        
        # dp = set()
        # dp.add(0)
        # target = sum(nums)//2

        # for i in range(len(nums)-1, -1, -1):
        #     nextDP = set()
        #     for t in dp:
        #         nextDP.add(t + nums[i])
        #         nextDP.add(t)
        #     dp = nextDP
        
        # return True if target in dp else False


















        # #bruteforce: check each subset see if total equals half the sum
        # if sum(nums) % 2:
        #     return False
        # target = sum(nums)/2
        
        # def dfs(i, total):
        #     if total == target:
        #         return True
        #     if i >= len(nums) or total > target:
        #         return False
            
        #     # # only valid if all nums are positive
        #     # if total > target:
        #     #     return False

        #     return dfs(i, total + nums[i]) or dfs(i + 1, total)

        # return dfs(0, 0)

        


