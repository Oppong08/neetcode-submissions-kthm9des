# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #j loops through resultant list until index,
        #check if value at index equals 
         #curr loops through given list 
        #[1] -> [2] -> [3] ->[4]-> [2]
        #res = ([1]-> [3])
        curr = head
        seen = set()
        while curr:
            if curr.val in seen:
                return True
            seen.add(curr.val) 
            curr = curr.next
        return False

        
        
        
            
        