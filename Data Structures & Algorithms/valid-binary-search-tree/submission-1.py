# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #logic: BST is valid if each node must is bigger than its left boundary but lower than the right boundary
        #the left boundary for left node's left node is - infinity and the right boundary for the left node is it's parent 
        #the left boundary for right node's left node is it's parent and grandparent and right boundary is positive infinity
        #traferse and update left and right boundaries appropriately 

        def valid(node,left_b, right_b):
            #base case: if node is none: return True
            if not node:
                return True
            if not (node.val < right_b and node.val > left_b):
                return False
            return (valid(node.left,left_b,node.val)) and (valid(node.right, node.val, right_b))

        return valid(root, float('-inf'), float('inf'))
