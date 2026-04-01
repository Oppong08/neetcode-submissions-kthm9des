# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #bfs return last element
        res = []
        q = deque()
        q.append(root)
        if not root:
            return res
        while q:
            res.append(q[-1].val)
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # res.append(node.val)
        return res   


        # #bfs return last element
        # res = []
        # q = deque()
        # q.append(root)
        # while q:
        #     rightside = None
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node:
        #             rightside = node
        #             q.append(node.left)
        #             q.append(node.right)
        #     if rightside:
        #         res.append(rightside.val)
        # return res   







        # #BFS: travers the nodes level order, at each level, rightSide is the right most value(last index popped)
        # #add ther rightSide's value to a result list
        
        # res = []
        # q = collections.deque([root])

        # while q:
        #     rightSide = None
        #     qLen = len(q)
        #     for i in range(qLen):
        #         node = q.popleft()
        #         if node:
        #             rightSide = node
        #             q.append(node.left)
        #             q.append(node.right)
        #     if rightSide:
        #         res.append(rightSide.val)
        # return res
