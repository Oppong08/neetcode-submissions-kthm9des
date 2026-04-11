# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            #handle negative where leftMax could include the negative number or not included (0)
            leftMax = max(leftMax, 0)
            rigthMax = max(rightMax, 0)

            #compute the max path sum WITH split
            res[0] = max(res[0], root.val + leftMax + rightMax)        

            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]
