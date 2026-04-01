class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        row = [1] * n
        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2,-1,-1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]




        # row,col = m,n
        # visited = set() 
        # res = 0
        # def dfs(r,c):
        #     if (r < 0 or r>=row or c<0 or c>=col or 
        #         (r,c) in visited):
        #         return
        #     visited.add((r,c))
        #     nonlocal res
        #     res += 1
        #     for r in range(row):
        #         for j in range(col):
        #             dfs(r + 1, c) + dfs(r, c + 1)
        #             res += 1
                    
        # dfs(0,0)
        # return res

    