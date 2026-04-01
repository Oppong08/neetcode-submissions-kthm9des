class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # each element is 1 greater than the previous
        #key, a number is the start of a sequence if its previous value(n-1) is not in the set
        numSet = set(nums)
        longest = 0
        for n in nums:
            #check if a number is the start of a sequence
            if (n-1) not in numSet:
                lenght  = 1 #starts calculating the length of the sequence

                while (n + lenght) in numSet:
                    lenght += 1
                longest = max(lenght, longest)
            
        return longest

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #sorting 
        nums.sort()
        longest = 1
        res = 1
        for r in range(1,len(nums)):
            if nums[r] == nums[r-1] + 1:
                res +=1
            
            else:
                longest = max(longest, res)
                res = 1
        return longest

        
