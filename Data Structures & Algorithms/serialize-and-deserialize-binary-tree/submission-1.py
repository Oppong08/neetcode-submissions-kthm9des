# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # traverse and convert to serialized format (strings)

        res = []

        def dfs(node):
            if node == None:
                res.append("N")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)





















        #     if not node:
        #         res.append("N")
        #         return
        #     res.append(str(node.val))
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)
        # return ",".join(res)
                
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #extract each value from data into a list
        vals = data.split(',')
        self.i = 0
        def dfs():     
        #dfs traverses the list of values, first converts the current value to a treenode and run dfs on it ( with i+=1) to build the left and right children(trees)
            for j in range(len(data)):
                #base case if we see N in our traversal, return None, stop current dfs and move to the next val
                if vals[self.i] == 'N':
                    self.i += 1
                    return
                node = TreeNode(int(vals[self.i]))
                self.i += 1
                node.left = dfs()
                node.right = dfs()

                return node

        return dfs()



        #extract each value from data, build the tree again
        # vals = data.split(",")
        # self.i = 0

        # def dfs():
        #     if vals[self.i] == "N":
        #         self.i += 1
        #         return None
            
        #     node = TreeNode(int(vals[self.i]))
        #     self.i += 1
        #     node.left = dfs()
        #     node.right = dfs()

        #     return node
        # return dfs()
 
