class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [-float('inf')]

        def dfs(root):
            if not root:
                return 0
            
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            #computer sum WITH double split allowed
            res[0] = max(res[0], rightMax + leftMax + root.val)

            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]



        # res = [root.val]

        # def dfs(root):
        #     if not root:
        #         return 0
            
        #     leftMax = dfs(root.left)
        #     rightMax = dfs(root.right)

        #     #handle negative where leftMax could include the negative number or not included (0)
        #     leftMax = max(leftMax, 0)
        #     rightMax = max(rightMax, 0)

        #     #compute the max path sum WITH split
        #     res[0] = max(res[0], root.val + leftMax + rightMax)        

        #     return root.val + max(leftMax, rightMax)
        
        # dfs(root)
        # return res[0]