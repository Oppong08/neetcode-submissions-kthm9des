# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res = []
        # def bfs(root):
        #     q = deque()
        #     q.append(root)
        #     while q:
        #         for i in range(len(q)):
        #             node = q.pop()
        #             if node.left:
        #                 q.append(node.left)
        #             elif node.right:
        #                 q.append(node.right)
            
        #             res.append(node.val)
        # bfs(root)
        # return res




        res = []
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res