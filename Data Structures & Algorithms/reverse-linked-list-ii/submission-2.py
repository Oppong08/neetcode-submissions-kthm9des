# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        cur, leftprev = head, dummy
        for i in range(left - 1):
            leftprev = cur
            cur = cur.next
        
        prev = None
        for i in range(right - left + 1):
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex

        leftprev.next.next = cur
        leftprev.next = prev

        return dummy.next


































        # dummy = ListNode(0,head)

        # #get a pointer to the left and the left previous nodes
        # leftprev, cur = dummy, head
        # for i in range(left-1):
        #     leftprev, cur = cur, cur.next

        # prev = None
        # for i in range(right - left + 1):
        #     tmpNext = cur.next
        #     cur.next = prev
        #     prev,cur = cur, tmpNext

        # leftprev.next.next = cur
        # leftprev.next = prev

        # return dummy.next



        











        
        #get l, r
        # cur = head
        # i = 0
        # while cur:
        #     l += 1
        #     if i == l:
        #         break
        #     cur = cur.next
        
        # leftnode = cur
        # j = i
        # while cur:
        #     j += 1
        #     if j == right:
        #         break
        #     cur = cur.next

        # dummy = leftnode.next
        # leftnode.next = cur.next

