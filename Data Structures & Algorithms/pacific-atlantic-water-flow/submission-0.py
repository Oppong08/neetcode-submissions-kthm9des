class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

       #logic: Instead of trying to move from each cell to the pacific and atlantic oceans respectively
       #move from the oceans to the board and mark all cells the water can flow to (cells greater heights than the previous cell)
       #put the marked cells in pacific and atlantic sets respectively
       #finally scan throught the entire grid and check which cells were in both sets, these represent the cells through which water from both oceans can flow to
       #add these cells to a result list and return the list

        #get dimensions of grid
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        #dfs function
        def dfs(r,c,visited,prevheight):
            #base case: if cell is out of bounds, visited before or has height less than previous height, return
            if (r<0 or c< 0 or r==rows or c==cols 
                or (r,c) in visited or heights[r][c]<prevheight):
                return
            
            #recursive: run dfs on all directions and mark as visited
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c,visited, heights[r][c])
            dfs(r, c+1,visited, heights[r][c])
            dfs(r, c-1,visited, heights[r][c])
            

        #run dfs on top and bottom edge cells
        for c in range(cols):
            dfs(0,c,pac, heights[0][c])
            dfs(rows-1,c,atl, heights[rows-1][c])
        
        #run dfs on first and last edge cells to for pacificwater flow
        for r in range(rows):
            dfs(r,0, pac, heights[r][0])
            dfs(r,cols-1, atl, heights[r][cols-1])
        
        res = []
        #go through each grid to add cells in both sets to results
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res
        
                

