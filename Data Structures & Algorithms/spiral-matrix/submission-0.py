class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #logic: set left and right pointers to track the boundaries of the current block we're working on
        #withing each block, iterate through in spiral order(from left to right,  then right to bottom, right to left and bottom to top) adding each cell item to a result store
        #the top and bottom pointers are then the updated to move to the next working block and the spiral traversal is repeated again
        #this while loop stops when either the left and the right pointers meet or the top and bottom pointers meet
        
        left, right = 0,len(matrix[0])     #right column padded
        top, bottom = 0, len(matrix)    #bottom row padded
        res = []
        while left < right and top < bottom:
            #move from left to right and add to res
            for i in range(left, right):
                res.append(matrix[top][i]) 
            top += 1        #update top row early to avoid mutiple count

            #move from top to down
            for i in range(top,bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break
            #move from right to left
            
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -=1

            #move from down to top
            for i in range(bottom - 1, top - 1,-1):
                res.append(matrix[i][left])
            left += 1

            
        return res
            


