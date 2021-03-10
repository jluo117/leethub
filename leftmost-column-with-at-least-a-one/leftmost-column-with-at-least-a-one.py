# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows,cols = binaryMatrix.dimensions()
        curRow = 0
        cols -= 1
        lastFound = -1
        while curRow < rows:
            if cols == -1:
                break
            while binaryMatrix.get(curRow,cols) == 1:
                lastFound = cols
                cols -= 1
                if cols == -1:
                    break
            curRow += 1
        return lastFound
            
            
                