class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        count = sum(matrix[0])
        for row in range(1,len(matrix)):
            if matrix[row][0] == 1:
                count += 1
            for col in range(1,len(matrix[row])):
                if matrix[row][col] == 1:
                    matrix[row][col] = min(matrix[row][col-1],matrix[row-1][col],matrix[row-1][col-1])+1
                    count += matrix[row][col]
        return count
                    
                