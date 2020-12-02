'''
f(x,y) = f(x+1,y) + f(x,y+1)
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = {}
        x = 0
        y = 0
        def helper(x,y):
            if (x,y) in table:
                return table[(x,y)]
            if y == m-1 and x == n-1:
                return 1
            pos = 0
            if x < n-1:
                pos += helper(x+1,y)
            if y < m-1:
                pos += helper(x,y+1)
            table[(x,y)] = pos
            return pos
        
        return helper(x,y)
                
        
        
