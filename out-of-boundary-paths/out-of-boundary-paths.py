class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        table = {}
        def helper(y,x,N):
            if (y,x,N) in table:
                return table[(y,x,N)]
            if y < 0:
                return 1
            if x < 0:
                return 1
            if y >= m:
                return 1
            if x >= n:
                return 1
            if N == 0:
                return 0
            res = helper(y-1,x,N-1) + helper(y,x-1,N-1)+helper(y+1,x,N-1) + helper(y,x+1,N-1)
            table[(y,x,N)] = res
            return res
        return helper(i,j,N) % (pow(10,9)+7)
            
            
        