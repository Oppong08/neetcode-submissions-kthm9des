# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #logic: the values in the preorder list give idea of the root of the tree and subsequent subtrees
        # the values in ther inorder list give idea on ther number nodes to complete a particular tree given it's root
        #find root from the preorder, for each root, find it's index(m) in the inorder:
        #values to the left of m makes the left subtree from that node and values to ther right of m makes the right subtree from that node
        #recursively build subsequent subtrees from respective halves, slicing out the current head

        #base case: if we reach the end of either preorder or inorder, return none
        if not preorder or not inorder:
            return None
        
        #start building, starting from the root which is always the first item in the inorder list
        root = TreeNode(preorder[0])

        #find index(m) in inorder to build each half of the subtrees
        m = inorder.index(preorder[0])
        
        #recursively build left using the next current head
        root.left = self.buildTree(preorder[1:m+1],inorder[:m + 1])
        #recursively build right subtree the next item after the current head
        root.right = self.buildTree(preorder[m+1:],inorder[m+1:])

        return root



