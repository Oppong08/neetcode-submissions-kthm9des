# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        dummy = res
        i = list1
        j = list2
        if not i :
            return j
        if not j:
            return i 
        while i and j:
            if i.val < j.val:
                res.next = i
                i = i.next
            else:
                res.next = j
                j = j.next
            res = res.next

        while j:
            res.next = j
            j = j.next 
            res = res.next
        
        while i:
            res.next = i
            i = i.next
            res = res.next
        return dummy.next
                
