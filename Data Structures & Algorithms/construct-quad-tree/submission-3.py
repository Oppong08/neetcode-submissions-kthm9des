"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        #define dfs(n,r, c)
        #check if all values in nxn grid starting from the current cell, if same return a leaf node
        #build tree recursively if not same.
        def dfs(n,r,c):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c+j]:
                        allSame = False
                        break
            if allSame:
                return Node(grid[r][c], True)
            #if all values in grid are not same, divide the grid into two and recursively build the tree
            n = n//2
            topleft = dfs(n,r,c)
            topright = dfs(n, r, c + n)
            bottomleft = dfs(n, r+n, c)
            bottomright = dfs(n, r+n, c+n)

            return Node(0, False, topleft, topright, bottomleft, bottomright)
        
        return dfs(len(grid), 0, 0)






















        # def dfs(n,r, c):
        #     allSame = True
        #     for i in range(n):
        #         for j in range(n):
        #             #if all cells are not the same
        #             if grid[r][c] != grid[r+i][c + j]:
        #                 allSame = False
        #                 break
        #     if allSame:
        #         return Node(grid[r][c], True)
            
        #     n = n//2
        #     topleft = dfs(n, r, c)
        #     topright = dfs(n, r, c + n)
        #     bottomleft = dfs(n, r + n, c)
        #     bottomright = dfs(n, r+n, c + n)
        #     return Node(0, False, topleft, topright, bottomleft, bottomright)
        # return dfs(len(grid), 0, 0,)
