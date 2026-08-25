# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #iterative dfs (simulate under the hood recursive stack)
        res = []
        stack = [] #stores the order of processing nodes
        cur = root

        while cur or stack:
            #searches the left subtree
            while cur:
                stack.append(cur)
                res.append(cur.val)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return res














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




        # res = []
        # def dfs(node):
        #     if not node:
        #         return
        #     res.append(node.val)
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)
        # return res