# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
       #root to x all less than x
       #start from the root, keep track of the max we've seen so far
       #increase count if a value is found greater than max, set this to new max
       #continue down the root if a node is less than the max so far

        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        return dfs(root, root.val)
        

        #     if not node:
        #         return 0


        #     if node.left.val > max:
        #         return 1 + dfs(node.left, node.left.val)
            
        #     else:
        #         dfs(node.left, max)
            
        #     if node.right.val > max:
        #         return 1 + dfs(node.right, node.right.val)
        #     else:
        #         dfs(node.right)
            

