class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r< 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
        # Rows, Col = len(board), len(board[0])
        # path = set()

        # def dfs(r,c,i):
        #     #if we reach the end of the word
        #     if i == len(word):
        #         return True
        #     #if we go out of bounds
        #     if (r < 0 or c<0 or r >= Rows or 
        #         c >= Col or board[r][c] != i or 
        #         (r,c) in path):
        #         return False

        #     #add to path
        #     path.add((r,c))
        #     res = (dfs((r+1,c, i+ 1)) or 
        #         dfs(r-1,c, i+ 1) or
        #         dfs(r+1,c+1, i+ 1) or
        #         dfs(r+1,c-1, i+ 1))
        #     path.remove((r,c))

        # for r in range(Rows):
        #     for c in range(Col):
        #         if dfs(r,c,0):
        #             return True
        # return False



