# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        #recursive post order traversal
        if not root:
            return None
        
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)

        #check if root is a leaf node and equal to target
        if not root.left and not root.right and root.val == target:
            return None
        
        return root

















        # def dfs(root):
        #     if not root:
        #         return None

        #     if root.val == target:
        #         #delete val
        #         if not root.left:
        #             return dfs(root.right)
                
        #         if not root.right:
        #             return dfs(root.left)

        #             #find successor
            
        #     #continue searching on root

            

            

        