class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        newMatrix = []
        if len(A) == 0:
            return []
        for col in range(len(A[0])):
            newRow = []
            for row in range(len(A)):
                newRow.append(A[row][col])
            newMatrix.append(newRow)
        return newMatrix
        
            
        
