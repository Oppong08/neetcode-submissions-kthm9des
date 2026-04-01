"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

       #goal: create exact copy(clone) of graph given its node
       #logic: have a hasmap to map each original node to it's copy
       #create a copy of the current node, recursively do same for its neigbors adding each neighbor copy to the new copy's list of neighbors
        clonemap = collections.defaultdict()
        def dfs(node):
            if node in clonemap:
                return clonemap[node]
            if not node:
                return None
            copy = Node(node.val)
            clonemap[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)






















        # #hasmaph mapping old to new copies
        # oldToNew = {}
        # def dfs(node):
        # #base case: if node has its copy in the map, return its copy
        #     if node in oldToNew:
        #         return oldToNew[node]
        #     #create a copy of first node and adds it to the map
        #     copy = Node(node.val)
        #     oldToNew[node] = copy

        #     #recursively clone each neighbor, adding to the neighbor list of each copy
        #     for nei in node.neighbors:
        #         copy.neighbors.append(dfs(nei))

        #     #return first copy after dfs
        #     return copy
        # return dfs(node) if node else None
        
                
            
                    



        
        

        

        
        


        