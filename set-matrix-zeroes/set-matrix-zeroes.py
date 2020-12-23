class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        maxValue = 0
        for row in matrix:
            maxValue = max(maxValue,max(row))
        maxValue += 1
        def setRowandCol(x,y):
            for rowIndex in range(len(matrix[y])):
                if matrix[y][rowIndex] == 0:
                    continue
                matrix[y][rowIndex] = maxValue
            for colIndex in range(len(matrix)):
                if matrix[colIndex][x] == 0:
                    continue
                matrix[colIndex][x] = maxValue
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] == 0:
                    setRowandCol(x,y)
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] == maxValue:
                    matrix[y][x] = 0
        """
        Do not return anything, modify matrix in-place instead.
        """
        
