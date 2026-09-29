# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #logic: isSubtree recursively on each subtree(starting from the head to all other nodes) against sburoot
        #same trees are automatically subtrees hence included as a helper function int the isSubtree function
        #isSubtree edge case: null is an subRoot of any non-empty tree and an empty root 
        #but an empty root can never have a non-empty subroot


        #base case 1: null is an subRoot of any non-empty tree and an empty root 
        if not subRoot: 
            return True

        #base case 2: an empty root can never have a non-empty subroot
        if not root :
            return False
        
        #recursive case: if current subroot is same, return True
        
        if self.sametree(root, subRoot):
            return True
        
        #call isSubtree recursively on the root of the next subtree(starting from the head to all other nodes) against subroot
        return (self.isSubtree(root.left, subRoot)) or (self.isSubtree(root.right, subRoot))

    #same tree helper function; used as one condition for checking for a subroot
    def sametree(self, r, s):
        if not r and not s:
            return True
        if r and s and r.val == s.val:
            return (self.sametree(r.left, s.left)) and (self.sametree(r.right, s.right))
        else:
            return False















        
        # def search(root):
        #     if not root:
        #         return 
        #     if root.val == subRoot.val:
        #         return root
        #     search(root.left)
        #     search(root.right)

        # def dfs(root, sub):
        #     if not root and not sub:
        #         return True
        #     if not root or not sub or root.val != sub.val:
        #         return False
        #     return (dfs(root.left, sub.left)) and (dfs(root.right, sub.right))

        # same = search(root)
        # return dfs(same, subRoot)
