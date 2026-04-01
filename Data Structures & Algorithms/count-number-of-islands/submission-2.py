class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #BFS
        if not grid :
            return 0
        
        #get dimenstions of grid
        rows, cols = len(grid), len(grid[0])
        #mark visited cells
        visited = set()
        #initialize number of islands
        isisland = 0

        # def bfs(r,c):
        #     q = collections.deque()
        #     visited.add((r,c))
        #     q.append((r,c))
            
        #     while q:
        #         row,col = q.popleft()
        #         directions = [[1,0],[-1, 0], [0,1],[0,-1]]
        #         for dr, dc in directions:
        #             r, c = row + dr, col + dc
        #             if (r in range(rows) and 
        #                 c in range(cols) and
        #                 grid[r][c] == '1' and 
        #                 (r, c) not in visited):
        #                 q.append((r, c))
        #                 visited.add((r, c))
        
        # #acess each grid, run bfs on it 
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == '1' and (r,c) not in visited:
        #             bfs(r,c)
        #             isisland +=1
        # return isisland
        

        #dfs
        def dfs(r,c):
            if (r < 0 or c < 0 or r>= rows or c>= cols or (r,c) in visited or grid[r][c] == "0"):
                return 
            # grid[r][c] = "0"
            visited.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r,c +1)
            dfs(r,c-1)



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c)
                    isisland += 1
        return isisland




