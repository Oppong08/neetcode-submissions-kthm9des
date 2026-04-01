# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #logic: run a BST search, ie. check which half of the tree the nodes could belong to and look that way only
        #stop when we see the lowest common ancestor. the lowest common ancestor is the node where:
        # 1. a split occurs, ie. p and q are in opposite directions from the node
        #2. the node same as p or q along the tree


        #Iterative:
        # cur = root
        # while cur:
        #     if p.val > cur.val and q.val > cur.val: #if both p and q are greater , look in the right half 
        #         cur = cur.right
        #     elif p.val < cur.val and q.val < cur.val: #if both p and q are greater , look in the left half 
        #         cur = cur.left 
        #     else: # where split occurs (one is greater and one is smaller) or we've reach the node itself
        #         return cur

        #recursive
        #same base case: 
        if not root or not p or not q: #if there's no common ancestor
            return 
        if p.val > root.val and q.val >root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val :
            return self.lowestCommonAncestor(root.left,p, q)
        else:
            return root

