# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #two pointers 
        #logic when the gap between the left an right pointers is n and maintained, left would be at a distance 
        #of n from the end of the list by the time right reaches the end of the list
        #hence left would be ponting to the nth node from the end 
        
        right = head         #initialize right to head  
        while n > 0 and right :     #then shift by n from left to set gap
            right = right.next
            n -=1
        
        dummy = ListNode(0,head)
        left = dummy              #initially left point to dummy so as to make deletion easier
        while right:
            right = right.next
            left = left.next
        
        #left would be pointing at the node before the nth node from the end hence making deletion easier
        left.next = left.next.next    
        return dummy.next      
            











        
        #double pass
        # dummy = ListNode()
        # dummy.next = cur = head
        # prev = dummy
        # i = 0
        # while cur:
        #     i +=1
        #     cur = cur.next
        # #i == len(list)
        # t = 0
        # cur2 = head
        # while cur2:
        #     if t == i - n:
        #         prev.next = cur2.next
        #         break
        #     t+=1
        #     prev = cur2
        #     cur2 = cur2.next
        # return dummy.next
        