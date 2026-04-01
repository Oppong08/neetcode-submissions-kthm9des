class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False


        # #determine which rows/cols need to be zero

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if matrix[r][c] == 0:
        #             matrix[0][c] = 0

        #             if r > 0:
        #                 matrix[r][0] = 0

        #             else:
        #                 rowZero = True
        
        # for r in range(1, ROWS):
        #     for c in range(1,COLS):
        #         if matrix[0][c]== 0 or matrix[r][0] == 0:
        #             matrix[r][c] = 0
                
        # if matrix[0][0] == 0:
        #     for r in range(ROWS):
        #         matrix[r][0] = 0

        # if rowZero:
        #     for c in range(COLS):
        #         matrix[0][c] = 0


        #bruteforce: create a copy of the original matrix, loop throught the original matrix to scan for zero
        #if a zero is found in the original matrix, the column and theo row at the position in the copy is set to zeros
        #finally copy back the zero-updated copy back into the original matrix

        ROWS, COLS = len(matrix), len(matrix[0])
        mark = [[matrix[r][c] for c in range(COLS)] for r in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    for col in range(COLS):
                        mark[r][col] = 0
                    for row in range(ROWS):
                        mark[row][c] = 0

        #add the copy back inot the original matrix
        for r in range(ROWS):
            for c in range(COLS):
                matrix[r][c] = mark[r][c]
        
        
       