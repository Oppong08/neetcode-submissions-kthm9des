# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #l.      
        #Input: head = [2,4,6,8,10]
        #n =                     r
        #Output: [2,10,4,8,6]
        #        0,4,1,3,2,
        # 
        #with extra space:
        #loop throught list and add each to different new list/array
        #add each theorem separately according to their position
        mlist = []
        curr = head
        while curr:
            mlist.append(curr)
            curr = curr.next

        l, r = 0, len(mlist) -1
        while l < r:
            mlist[l].next = mlist[r]
            l += 1
            # if l >= r:
            #     break
            mlist[r].next = mlist[l]
            r -= 1
            
        mlist[l].next = None
            

            
            


        



