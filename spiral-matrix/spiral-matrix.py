class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def leftToRight(L,R,row):
            res = []
            for i in range(L,R+1):
                res.append(matrix[row][i])
            return res
        def topToBot(h,l,col):
            res = []
            for i in range(h+1,l+1):
                res.append(matrix[i][col])
            return res
        def rightToLeft(R,L,row):
            res = []
            for i in range(R-1,L-1,-1):
                res.append(matrix[row][i])
            return res
        def botToTop(l,h,col):
            
            res = []
            for i in range(l-1,h,-1):
                res.append(matrix[i][col])
            return res
        if len(matrix) == 0:
            return 0
        high = 0
        low = len(matrix)-1
        left = 0
        right = len(matrix[0])-1
        res = []
        while high <= low and left <= right:
            res += (leftToRight(left,right,high))
            res += (topToBot(high,low,right))
            if high != low:
                res += (rightToLeft(right,left,low))
            if right != left:
                
                res += (botToTop(low,high,left))
            high += 1
            low -= 1
            left += 1
            right -= 1
        return res
        
            
        