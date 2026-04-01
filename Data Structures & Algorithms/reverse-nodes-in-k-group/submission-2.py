# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        #logic: create a helper function to find the kth node, keep track of the next kth value as the start of the next group(GroupNext), 
        #reverse the nodes starting the group's first item to kth (GroupPrev). The group's first item's (GroupPrev) next points to kth.next
        #the kth node becomes the head of the first group(GroupPrev points to kth node after reversal),

    #     dummy = ListNode(0,head) #tracks the head of the entire node
    #     GroupPrev = dummy #dummy(Node just beforef the current group) for traversing the start of the current group
    #     while True:
    #         kth = self.getKth(GroupPrev, k)
    #         if not kth:
    #             break
    #         groupNext = kth.next
    #         #reverse starting GroupPrev
    #         curr = GroupPrev.next
    #         prev = kth.next
    #         while curr != groupNext:
    #             tmp = curr.next
    #             curr.next = prev
    #             prev = curr
    #             curr = tmp
            

    #         #after reversing
    #         tmp = GroupPrev.next
    #         GroupPrev.next = kth
    #         groupPrev = tmp

    #     return dummy.next


    # def getKth(self, curr, k):
    #     while curr and k > 0:
    #         curr = curr.next
    #         k-=1 
    #     return curr






        dummy = ListNode(0, head)
        groupPrev = dummy  #first element from the previous group 

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
        
            groupNext = kth.next #Node after the current group 

            #reverse group
            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr