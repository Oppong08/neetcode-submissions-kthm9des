# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #base case 1: if not node, return True
        if not root: 
            return True
        #base case2: if left node is bigger or right node is smaller
        if root.left and root.right:
            if (root.left.val > root.val) or (root.right.val < root.val):
                return False
        return (self.isValidBST(root.left)) and (self.isValidBST(root.right))
       