class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        curRow = len(matrix) -1
        while curRow >= 0:
            row = curRow
            col = 0
            expectedVal = None
            while row < len(matrix) and col < len(matrix[row]):
                if expectedVal == None:
                    expectedVal = matrix[row][col]
                if expectedVal != matrix[row][col]:
                    return False
                row += 1
                col += 1
            curRow -= 1
        curCol = 1
        while curCol < len(matrix[0]):
            row = 0
            col = curCol
            expectedVal = None
            while row < len(matrix) and col < len(matrix[row]):
                if expectedVal == None:
                    expectedVal = matrix[row][col]
                if expectedVal != matrix[row][col]:
                    return False
                row += 1
                col += 1
            curCol += 1
        return True
                
        
