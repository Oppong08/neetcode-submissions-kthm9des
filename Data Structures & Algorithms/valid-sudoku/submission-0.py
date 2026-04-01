class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #plan: loop each row to check for repeatition
        # loop each column to check for possible repeatition
        #check 3 X 3 box by cheacking each row//3 and column//3 as they'll give the same result in each box number 
        colset = defaultdict(set)
        rowsset = defaultdict(set)
        squaresset = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rowsset[r] or board[r][c] in colset[c] or board[r][c] in squaresset[(r//3,c//3)]):
                    return False

                colset[c].add(board[r][c])
                rowsset[r].add(board[r][c])
                squaresset[(r//3,c//3)].add(board[r][c])
                
        return True


                
        

        