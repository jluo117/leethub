class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        curRow = len(matrix) -1
        while curRow >= 0:
            row = curRow
            col = 0
            diagonal = []
            while row < len(matrix) and col < len(matrix[row]):
                diagonal.append(matrix[row][col])
                row += 1
                col += 1
            if sum(diagonal)/len(diagonal) != diagonal[0]:
                return False
            curRow -= 1
        curCol = 1
        while curCol < len(matrix[0]):
            row = 0
            col = curCol
            diagonal = []
            while row < len(matrix) and col < len(matrix[row]):
                diagonal.append(matrix[row][col])
                row += 1
                col += 1
            if sum(diagonal)/len(diagonal) != diagonal[0]:
                return False
