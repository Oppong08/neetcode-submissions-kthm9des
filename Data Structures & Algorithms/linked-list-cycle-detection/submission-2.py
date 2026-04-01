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
            if curr in seen:
                return True
            seen.add(curr) 
            curr = curr.next
        return False

        #slow and fast pointer technique(floyd's tortise and hare)
        slow, fast = 0, 0 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
            
        
            
        