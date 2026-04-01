class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return nums[i]
        
        #linked list(Floyd's tortoise and hare algorithm)
        #Logic: find the point of intersection using floyds tortoise and hare algorithm
        #start a new slow pointer, move it with the old(cycle) slow pointer towards each other, one step at a time
        #the point of intersection between the two slow pointers(second point of intersection), ie the entry point of the cycle is the duplicate number

        slow, fast = 0,0

        while True:
            slow = nums[slow] #move slow by one step 
            fast = nums[nums[fast]] #mover fast by two steps
            if fast == slow:
                break
            
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                return slow 



















        # slow, fast = 0, 0
        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow == fast:
        #         break
        
        # slow2 = 0
        # while True:
        #     slow = nums[slow]
        #     slow2 = nums[slow2]
        #     if slow == slow2:
        #         return slow
