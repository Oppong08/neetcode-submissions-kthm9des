# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #calcuate diameter = length of longest path

        res = 0
        def dfs(node):
            if not node:
                return 0
            
            nonlocal res
            left = dfs(node.left) 
            right = dfs(node.right) 
            res = max(res, left + right)

            return 1 + max(dfs(node.left), dfs(node.right))
        dfs(root)
        return res



            





























        # res = 0

        # #returns height
        # def dfs(root):
        #     if root == None:
        #         return 0
        #     left = dfs(root.left)
        #     right = dfs(root.right)

        #     nonlocal res
        #     res = max(res, left + right)#l+r calculates the longest connecting subtrees
        #     return 1 + max(left,right)
        # dfs(root)
        # return res
