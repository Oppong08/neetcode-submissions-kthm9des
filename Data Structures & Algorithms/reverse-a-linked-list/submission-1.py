# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev

        
































                    #prev. c
        # Input: head =  [0,1,2,3]
        # Output:        [3,2,1,0]

        #dummy = ListNode()
        # curr = head
        # prev = None
        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        # return prev






















        # iterative:
        # prev = None 
        # curr = head
        # while curr:
        #     temp = curr.next 
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        # return prev

        #recursive
        
        