# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #base case
        if not root:
            return root
        
        #search right if key is greater than root.val
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        #search left if key is less than root.val
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        #if key == root.val
        else:
            #if node to be deleted has no left child, return the right child
            if not root.left:
                return root.right

            #if it has no right child, return the left child
            elif not root.right:
                return root.left

            #if node to be deleted has both left and right children, find the inorder successor (the leftmost node in the right subtree)

            #find the min from the right subtree
            cur = root.left
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.left = self.deleteNode(root.left, root.val)

        return root






        
        # #traverse to find node
        # def traverse(node):
        #     if not node:
        #         return
    
        #     if key < node.val:
        #         node.left = traverse(node.left)
        #     elif key > node.val
        #         node.right = traverse(node.right)

        #     else: #found the key
        #         if not node.left:
        #             node.l

        # # if node has no right child, left succeeds

        # # if has no left child, right succeeds

        # # if has both left and right children