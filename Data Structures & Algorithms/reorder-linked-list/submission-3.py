# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #with extra space:
        #       l 
        #[0,1,2,3,4,5,6]
        #  0 -> 6 -> 1 -> 2     #r
        # if not head:
        #     return

        # num_list = []
        # curr = head
        # while curr:
        #     num_list.append(curr)
        #     curr = curr.next
        
        # #new_list = dummy = num_list[0] no need
        # l, r = 0, len(num_list) - 1

        # while l < r:
        #     num_list[l].next = num_list[r]
        #     l +=1

        #     # if l >= r:
        #     #     break
        #     num_list[r].next = num_list[l]
        #     r-1
    
        # num_list[l].next = None
        # # return 





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

        #Optimal:
        #break the list into two, reverse the later part and join

        # slow, fast = head, head.next
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
            

        # second = slow.next
        # prev = slow.next = None
        # while second:
        #    temp = second.next
        #    second.next = prev
        #    prev = second
        #    second = temp
        
        # #merge
    
        # first, second = head, prev
        # while second:
        #     t1 = first.next
        #     t2 = second.next
        #     first.next = second
        #     second.next = t1
        #     first = t1
        #     second = t2
            

        
        


            

            
            


        



