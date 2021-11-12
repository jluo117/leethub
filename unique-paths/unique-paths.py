class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = {}
        def helper(x,y):
            if (x,y) in table:
                return table[(x,y)]
            if x == m-1 and y == n-1:
                return 1
            pos = 0
            if x + 1 < m:
                pos += helper(x+1,y)
            if y + 1 < n:
                pos += helper(x,y+1)
            table[(x,y)] = pos
            return pos
        return helper(0,0)