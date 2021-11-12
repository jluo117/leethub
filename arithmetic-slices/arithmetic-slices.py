class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        gapDif = []
        lastVal = None
        for num in A:
            if lastVal == None:
                lastVal = num
                continue
            gapDif.append(num-lastVal)
            lastVal = num
        count = 0
        tol = 0
        for index in range(len(gapDif)):
            if index > 0 and gapDif[index-1] == gapDif[index]:
                count += 1
            else:
                count = 1
            
            tol += count -1
        return tol
                
            