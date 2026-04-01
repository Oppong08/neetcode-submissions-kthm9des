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
       #start count as 1 if a root's value isgreater than max else 0, update new max
       #continue runing dfs down the root and add count to it, return count(res) at the end of the dfs

        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        return dfs(root, root.val)
        

    

