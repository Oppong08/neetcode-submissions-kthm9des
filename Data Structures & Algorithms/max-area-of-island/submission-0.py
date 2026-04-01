class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # if not grid :
        #     return 0
        
        #get dimenstions of grid
        rows, cols = len(grid), len(grid[0])
        #mark visited cells
        visited = set()
        #initialize area
        #dfs
        def dfs(r,c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c] == 0):
                return 0
            # grid[r][c] = "0"
            visited.add((r,c))
            return (1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r,c+1) + dfs(r,c-1))

        res = 0
        for r in range(rows):
            for c in range(cols):
                #if grid[r][c] == '1' and (r,c) not in visited:
                    res = max(res, dfs(r,c))
        return res

        # def bfs(r,c):
        #     q = collections.deque()
        #     visited.add((r,c))
        #     q.append((r,c))
        #     res = 1
        #     while q:
        #         row,col = q.popleft()
        #         directions = [[1,0],[-1, 0], [0,1],[0,-1]]
        #         for dr, dc in directions:
        #             r, c = row + dr, col + dc
        #             if (r<0 or c< 0 or
        #                 r >= rows or c >= cols or
        #                 grid[r][c] == '0' or 
        #                 (r, c) in visited):
        #                 continue
        #             q.append((r, c))
        #             visited.add((r, c))
        #             res+=1
        #     return res
        
        # #acess each grid, run bfs on it 
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == '1' and (r,c) not in visited:
        #             res = max(res,bfs(r,c))
                    
                  
                    
        # return res