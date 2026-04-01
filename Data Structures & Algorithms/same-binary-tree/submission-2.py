# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     # if not p and not q:
    #     #     return True
    #     # if p and q and p.val == q.val:
    #     #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    #     # else:
    #     #     return False
    #  #base cases:1.if both nodes are empty
    #     if not p and not q: 
    #         return True
    # #2. if only one node is empty, or not equal return False
    #     if not p or not q or p.val != q.val: 
    #         return False
    # #recursive case, also our return value
    #     return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right,q.right))

        #BFS
        q1 = collections.deque([p])
        q2 = collections.deque([q])
        
        while q1 and q2:
            for _ in range(len(q1)):
                nodeP = q1.popleft()
                nodeQ = q2.popleft()
                
                if nodeP is None and nodeQ is None:
                    continue

                if nodeP is None or nodeQ is None or nodeP.val!=nodeQ.val:
                    return False

                q1.append(nodeP.left)
                q1.append(nodeP.right)
                q2.append(nodeQ.left)
                q2.append(nodeQ.right)
        
        return True
                
            

    
            