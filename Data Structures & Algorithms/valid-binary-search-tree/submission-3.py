# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #logic: BST is valid if each node must is bigger than its left boundary and lower than the right boundary
        #For BST in general Left subtree: values strictly less than the node. Right subtree: values strictly greater than the node
        # for nodes on the left subtrees, they left boundary is -infinity for left left nodes and the parent node for left right nodes
        #the right boundary is the parent node for left left nodes and inherited grandparent node for left right nodes
        #for nodes on the right, the left boundary is the parent node for right right nodes and inherited grandparent nodes for right left nodes
        #ther right boundary is infinity for right right nodes and the parent node for right left nodes
        #traverse and update left and right boundaries appropriately : hence our algorithm updates manually the right_boundary for left nodes, 
        #with the left_boundary for inheritance starting from infinty
        #it also updates manually the  left_boundary for right nodes, with the right_boundary for inheritance starting from infinity

        def valid(node, left, right):
            if not node:
                return True
            
            if not (left < node.val < right):
                return False
            
            return (valid(node.left,left,node.val)) and (valid(node.right,node.val,right))
    
        return valid(root, float('-inf'), float('inf'))




        # def valid(node,left_b, right_b):
        #     #base case: if node is none: return True
        #     if not node:
        #         return True
        #     if not (node.val < right_b and node.val > left_b):
        #         return False
        #     return (valid(node.left,left_b,node.val)) and (valid(node.right, node.val, right_b))

        # return valid(root, float('-inf'), float('inf'))
        