class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        table = {}
        def helper(cord):
            if cord in table:
                return table[cord]
            curVal = matrix[cord[0]][cord[1]]
            maxPos = 0
            if cord[0] < len(matrix)-1:
                if matrix[cord[0]+1][cord[1]] > curVal:
                    maxPos = max(helper((cord[0]+1,cord[1])),maxPos)
            if cord[0] > 0:
                if matrix[cord[0]-1][cord[1]] > curVal:
                    maxPos = max(helper((cord[0]-1,cord[1])),maxPos)
            if cord[1] < len(matrix[cord[0]])-1:
                if matrix[cord[0]][cord[1]+1] > curVal:
                    maxPos = max(helper((cord[0],cord[1]+1)),maxPos)
            if cord[1] > 0:
                if matrix[cord[0]][cord[1]-1] > curVal:
                    maxPos = max(helper((cord[0],cord[1]-1)),maxPos)
            table[cord] = maxPos + 1
            return maxPos + 1
        
        maxPos = 0
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                maxPos = max(maxPos,helper((y,x)))
        return maxPos
                
        
