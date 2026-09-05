# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #recursive
        if not root: #if root is null, create a new node and return
            return TreeNode(val)

        #if val is greater than root.val, recursively insert into the right subtree and update root.right with the result
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        #otherwise, recursively insert into the left subtree and update root.left
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root

        
        