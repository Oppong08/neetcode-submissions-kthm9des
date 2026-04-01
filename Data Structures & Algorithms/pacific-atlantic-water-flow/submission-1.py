class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:


       #logic: Instead of trying to move from each cell to the pacific and atlantic oceans respectively
       #move from the oceans to the board and mark all cells the water can flow to (cells greater heights than the previous cell)
       #put the marked cells in pacific and atlantic sets respectively
       #finally scan throught the entire grid and check which cells were in both sets, these represent the cells through which water from both oceans can flow to
       #add these cells to a result list and return the list

        #get dimensions of grid
        #rows, cols = len(heights), len(heights[0])
        # pac, atl = set(), set()

        # #dfs function
        # def dfs(r,c,visited,prevheight):
        #     #base case: if cell is out of bounds, visited before or has height less than previous height, return
        #     if (r<0 or c< 0 or r==rows or c==cols 
        #         or (r,c) in visited or heights[r][c]<prevheight):
        #         return
            
        #     #recursive: run dfs on all directions and mark as visited
        #     visited.add((r,c))
        #     dfs(r+1, c, visited, heights[r][c])
        #     dfs(r-1, c,visited, heights[r][c])
        #     dfs(r, c+1,visited, heights[r][c])
        #     dfs(r, c-1,visited, heights[r][c])
            

        # #run dfs on top and bottom edge cells
        # for c in range(cols):
        #     dfs(0,c,pac, heights[0][c])
        #     dfs(rows-1,c,atl, heights[rows-1][c])
        
        # #run dfs on left and right edge cells to for pacificwater flow
        # for r in range(rows):
        #     dfs(r,0, pac, heights[r][0])
        #     dfs(r,cols-1, atl, heights[r][cols-1])
        
        # res = []
        # #go through each grid to add cells in both sets to results
        # for r in range(rows):
        #     for c in range(cols):
        #         if (r,c) in pac and (r,c) in atl:
        #             res.append([r,c])

        # return res
        
    
    #BFS: inward flow
    #logic: BFS uses a 2D array to store marked cells in pacific and atlantic arrays as sets are used in dfs
    #first add all the edge cells to the que, and while popping each cell, mark it and add other cells that meets required conditions to the que
    #finally move throught the grid, checking for cells marked True in both pacific and atlantic arrays and adding those cells to results
    
    #create 2D array to store pacific and atlantic cells respectively

   

        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and
                        not ocean[nr][nc] and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        q.append((nr, nc))

        pacific = []
        atlantic = []
        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))

        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res       
        
        



