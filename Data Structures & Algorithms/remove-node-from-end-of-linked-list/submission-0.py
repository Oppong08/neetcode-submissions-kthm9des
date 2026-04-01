# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = cur = head
        prev = dummy
        i = 0
        while cur:
            i +=1
            cur = cur.next
        #i == len(list)
        t = 0
        cur2 = head
        while cur2:
            if t == i - n:
                prev.next = cur2.next
                break
            t+=1
            prev = cur2
            cur2 = cur2.next
        return dummy.next
        