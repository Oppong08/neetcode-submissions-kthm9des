# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #base cases:1.if both nodes are empty
        if not p and not q: 
            return True
    #2. if only one node is empty, or not equal return False
        if not p or not q or p.val != q.val: 
            return False
    #recursive case, also our return value
        return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right,q.right))


    
            