class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        table = {}
        def helper(y,x):
            if (y,x) in table:
                return table[(y,x)]
            if (y==len(grid)-1 and x ==len(grid[y])-1):
                return grid[y][x]
            minPath = float('inf')
            if y < len(grid)-1:
                minPath = min(minPath,helper(y+1,x)+grid[y][x])
            if x < len(grid[y])-1:
                minPath = min(minPath,helper(y,x+1)+grid[y][x])
            table[(y,x)] = minPath
            return minPath
        return helper(0,0)
            
        