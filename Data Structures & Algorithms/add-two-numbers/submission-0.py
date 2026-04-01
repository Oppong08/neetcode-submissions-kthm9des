# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy  #tracks where in our new list we've built up to 
        carry = 0 
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0 #gets the individual values whe want to ad
            v2 = l2.val if l2 else 0
            
            #new digit
            val = v1 + v2 + carry
            carry = val//10    #get's new carry after adding
            val = val % 10      #get's value to record if the results of addition is > 10
            cur.next = ListNode(val)

            #move to the next
            cur = cur.next
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None

        return dummy.next

            
