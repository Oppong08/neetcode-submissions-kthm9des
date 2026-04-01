class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Bitwise XOR:
        #logic: if we XOR all numbers from 0 to n and all numbers present in the array, every number that appears in both will cancel out leaving only the missing number
        #let n be the leng th of the array, for each index from 0 to n-1:
        #XOR result with i, XOR reseult with nums[i]
        #after the loop, result will contain the missing number
        n = len(nums)
        xorr = n
        for i in range(n):
            xorr^=i ^ nums[i]
        return xorr






        # #sorting O(nlogn) time, O(1)space
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] != i:
        #         return i
        # return len(nums)

        #hash set   O(n) space O(n) time
        # num_set = set(nums)
        # for i in range(len(nums)+1):
        #     if i not in num_set:
        #         return i
        
        #math
        #logic: if we subtract the sum of the given array fromn the expected sum of numbers from 0 to n, the result must be the missing number
        #Let n be the lenght of the array(start of our expected sum) and set res to n
        #for each index i from 0 to n-1, add i to res and subtract nums[i] from res
        #after the loop, res will hold the missing number
        # res = len(nums)
        # for i in range(len(nums)):
        #     res+=(i-nums[i])
        # return res