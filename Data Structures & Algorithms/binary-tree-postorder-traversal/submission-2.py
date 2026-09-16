# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack =[root]
        visit= [False] #tracks whether a node has been visited already or not
        res = []
        
        while stack: 
            cur, v = stack.pop(), visit.pop()
            if cur:
                if v:
                    res.append(cur.val)

                else:
                    stack.append(cur) #append root first
                    visit.append(True)
                    stack.append(cur.right) #append right first before left onto the stack
                    visit.append(False)
                    stack.append(cur.left) #append left last(rocess first before right)
                    visit.append(False)
                    cur = cur.left
        return res  








        # res = []
        # def dfs(node):
        #     if not node:
        #         return
        #     dfs(node.left)
        #     dfs(node.right)
        #     res.append(node.val)
        
        # dfs(root)
        # return res

        # #iterative dfs:
        # stack = [root]
        # res = []
        # visit = [False]
      
        # while stack:
        #     #only append nodes at the second visit
        #     cur, v = stack.pop(), visit.pop()
        #     if cur:
        #         if v:
        #             res.append(cur.val)
        #         else:
        #             stack.append(cur)
        #             visit.append(True)
        #             stack.append(cur.right)
        #             visit.append(False)
        #             stack.append(cur.left)
        #             visit.append(False)
        # return res




