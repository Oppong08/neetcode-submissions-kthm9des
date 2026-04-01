"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #logic: Two pass algorithm, first pass creates a copy of the cur node and maps each cur node to their copy
        #secon map sets the pointers of each copied node to the copies of the next pointers of each cur node

        cmap = {None: None}   #map nodes to their copy

        curr = head
        while curr:
            copy = Node(curr.val)
            cmap[curr] = copy
            curr = curr.next


        curr = head
        while curr:
            copynext = cmap.get(curr.next)
            cmap[curr].next = copynext
            cmap[curr].random = cmap[curr.random] 
            curr = curr.next
        
        return cmap[head]









        # oldToCopy = {None: None}
        
        # cur = head
        # while cur:
        #     copy = Node(cur.val)
        #     oldToCopy[cur] = copy
        #     cur = cur.next
        
        # cur = head
        # while cur:
        #     copy = oldToCopy[cur]
        #     copy.next = oldToCopy[cur.next]
        #     copy.random = oldToCopy[cur.random]   
        #     cur = cur.next

        # return oldToCopy[head]