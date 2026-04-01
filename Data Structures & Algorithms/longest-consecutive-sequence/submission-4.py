class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # each element is 1 greater than the previous
        #key, a number is the start of a sequence if its previous value(n-1) is not in the set
        # numSet = set(nums)
        # longest = 0
        # for n in nums:
        #     #check if a number is the start of a sequence
        #     if (n-1) not in numSet:
        #         lenght  = 1 #starts calculating the length of the sequence

        #         while (n + lenght) in numSet:
        #             lenght += 1
        #         longest = max(lenght, longest)
            
        # return longest

        
        
    
        
        #sorting 
        if not nums:
            return 0
        nums.sort()
        #need three pointers:
        res = 0   #tracks result/max sequence
        curr = nums[0] #keeps track on the current number we're on/expect
        streak = 0 #track streak
        i = 0 #starting index

        while i < len(nums):
            if curr != nums[i]: #checks if the nums[i] is not the expected next number
                curr = nums[i] #resets current to break sequence
                streak = 0 #resets streak back to 0
            while i < len(nums) and nums[i] == curr: #skips duplicates
                i += 1
            streak += 1 #continue streak
            curr += 1 #sets the current to the next expected 
            res = max(res, streak)
        return res
            



        
